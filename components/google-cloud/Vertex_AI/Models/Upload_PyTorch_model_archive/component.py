from typing import NamedTuple

from cloud_pipelines.components import create_component_from_func, InputPath, OutputPath


def upload_PyTorch_model_archive_to_Google_Cloud_Vertex_AI(
    model_archive_path: InputPath("PyTorchModelArchive"),
    torchserve_version: str = "0.6.0",
    use_gpu: bool = False,

    display_name: str = None,
    description: str = None,

    # Uncomment when anyone requests these:
    # instance_schema_uri: str = None,
    # parameters_schema_uri: str = None,
    # prediction_schema_uri: str = None,
    # explanation_metadata: "google.cloud.aiplatform_v1.types.explanation_metadata.ExplanationMetadata" = None,
    # explanation_parameters: "google.cloud.aiplatform_v1.types.explanation.ExplanationParameters" = None,

    project: str = None,
    location: str = None,
    labels: dict = None,
    # encryption_spec_key_name: str = None,
    staging_bucket: str = None,
) -> NamedTuple("Outputs", [
    ("model_name", "GoogleCloudVertexAiModelName"),
    ("model_dict", dict),
]):
    import json
    import os
    from google.cloud import aiplatform

    if not location:
        location = os.environ.get("CLOUD_ML_REGION")

    if not labels:
        labels = {}
    labels["component-source"] = "github-com-ark-kun-pipeline-components"

    container_image_tag = torchserve_version + "-" + ("gpu" if use_gpu else "cpu")
    container_image_uri = f"pytorch/torchserve:{container_image_tag}"

    # Vertex Endpoints refuse to support non-Google container registries.
    # We have to work around this to reduce user frustration
    # TODO: Remove this code when Vertex Endpoints service starts supporting other container registries.
    def copy_container_image(
        src_container_image_uri: str,
        dst_container_image_uri: str,
        project_id: str,
    ):
        from google.cloud.devtools import cloudbuild
        from google import protobuf
        build_client = cloudbuild.CloudBuildClient()
        build_config = cloudbuild.Build(
            images=[dst_container_image_uri],
            steps=[
                cloudbuild.BuildStep(
                    name="gcr.io/cloud-builders/docker",
                    entrypoint="bash",
                    args=[
                        "-exc",
                        'docker pull --quiet "$0" && docker tag "$0" "$1"',
                        src_container_image_uri,
                        dst_container_image_uri,
                    ],
                ),
            ],
            timeout=protobuf.duration_pb2.Duration(
                seconds=1800,
            ),
        )
        build_operation = build_client.create_build(
            project_id=project_id,
            build=build_config,
        )
        try:
            result = build_operation.result()
        except:
            print(f"Logs are available at [{build_operation.metadata.build.log_url}].")
            raise
        return result

    project_id = aiplatform.initializer.global_config.project
    mirrored_container_uri = f"gcr.io/{project_id}/container_mirror/{container_image_uri}"
    # FIX: Only mirror when image does not exist
    # docker does is unable to get the registry data from inside container (it cannot connecto to docker socket):
    # docker.errors.DockerException: Error while fetching server API version: ('Connection aborted.', FileNotFoundError(2, 'No such file or directory'))
    # import docker
    # try:
    #     docker_client = docker.from_env()
    #     docker_client.images.get_registry_data(mirrored_container_uri)
    # except docker.errors.NotFound:
    if True:
        print(f"Mirroring {container_image_uri} to {mirrored_container_uri}")
        copy_container_image(
            src_container_image_uri=container_image_uri,
            dst_container_image_uri=mirrored_container_uri,
            project_id=project_id,
        )
    container_image_uri = mirrored_container_uri
    # End of container image mirroring code

    model_archive_file_name = os.path.basename(model_archive_path)
    model_archive_dir = os.path.dirname(model_archive_path)

    model = aiplatform.Model.upload(
        # FIX: Use public image or mirror the official image
        #serving_container_image_uri="gcr.io/avolkov-31337/mirror/pytorch/torchserve",
        serving_container_image_uri=container_image_uri,
        artifact_uri=model_archive_dir,
        serving_container_command=[
            "bash",
            "-exc",
            '''
model_archive_uri="$0"
#model_archive_local_path=$(mktemp --suffix ".mar")
# For some reason the model must already be inside the model-store directory.
model_archive_local_path=./model-store/model.mar

# Downloading the model archive from GCS
# TODO: Fix gsutil bugs (requires project ID, has auth issues) and use gsutil instead.
# gsutil cp "$model_archive_uri" "$model_archive_local_path"
pip install google-cloud-storage
python -c '
import sys
from google.cloud import storage

model_archive_uri = sys.argv[1]
model_archive_local_path = sys.argv[2]

storage_client = storage.Client()
blob = storage.Blob.from_string(uri=model_archive_uri, client=storage_client)
blob.download_to_filename(filename=model_archive_local_path)
' "$model_archive_uri" "$model_archive_local_path"

#Note: config.properties is owned by root. Our user is not root.
echo "
service_envelope=json
# Needed for external access
inference_address=http://0.0.0.0:8080
management_address=http://0.0.0.0:8081
" > config2.properties
torchserve --start --foreground --no-config-snapshots --models main-model="$model_archive_local_path" --model-store ./model-store/ --ts-config config2.properties
            ''',
            "$(AIP_STORAGE_URI)/" + model_archive_file_name,
        ],
        serving_container_predict_route="/predictions/main-model",
        #serving_container_predict_route="/v1/models/main-model:predict",
        serving_container_health_route="/ping",
        serving_container_ports=[8080],

        display_name=display_name,
        description=description,

        # instance_schema_uri=instance_schema_uri,
        # parameters_schema_uri=parameters_schema_uri,
        # prediction_schema_uri=prediction_schema_uri,
        # explanation_metadata=explanation_metadata,
        # explanation_parameters=explanation_parameters,

        project=project,
        location=location,
        labels=labels,
        # encryption_spec_key_name=encryption_spec_key_name,
        staging_bucket=staging_bucket,
    )
    model_json = json.dumps(model.to_dict(), indent=2)
    print(model_json)
    return (model.resource_name, model_json)


if __name__ == "__main__":
    upload_PyTorch_model_to_Google_Cloud_Vertex_AI_op = create_component_from_func(
        func=upload_PyTorch_model_archive_to_Google_Cloud_Vertex_AI,
        base_image="python:3.9",
        packages_to_install=[
            "google-cloud-aiplatform==1.13.1",
            "google-cloud-build==3.8.3", # For container image mirroring
            #"docker==5.0.3", # For container image mirroring
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Upload_PyTorch_model_archive/component.yaml",
        },
        output_component_file="component.yaml",
    )
