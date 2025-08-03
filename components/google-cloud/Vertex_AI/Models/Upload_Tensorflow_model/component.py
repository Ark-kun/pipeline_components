from typing import NamedTuple

from cloud_pipelines.components import create_component_from_func, InputPath, OutputPath


def upload_Tensorflow_model_to_Google_Cloud_Vertex_AI(
    model_path: InputPath("TensorflowSavedModel"),
    tensorflow_version: str = None,
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

    model = aiplatform.Model.upload_tensorflow_saved_model(
        saved_model_dir=model_path,
        tensorflow_version=tensorflow_version,
        use_gpu=use_gpu,

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
    # Getting input descriptions
    # try:
    #     from google.cloud import aiplatform
    #     upload_Tensorflow_model_to_Google_Cloud_Vertex_AI.__doc__ = aiplatform.Model.upload_tensorflow_saved_model.__doc__
    # except ImportError:
    #     pass

    upload_Tensorflow_model_to_Google_Cloud_Vertex_AI_op = create_component_from_func(
        func=upload_Tensorflow_model_to_Google_Cloud_Vertex_AI,
        base_image="python:3.9",
        packages_to_install=[
            "google-cloud-aiplatform==1.16.0",
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Upload_Tensorflow_model/component.yaml",
        },
        output_component_file="component.yaml",
    )
