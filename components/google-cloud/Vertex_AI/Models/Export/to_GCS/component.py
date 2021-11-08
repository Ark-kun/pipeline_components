from typing import NamedTuple

from kfp.components import create_component_from_func


def export_model_to_GCS_for_Google_Cloud_Vertex_AI_Model(
    model_name: "GoogleCloudVertexAiModelName",
    output_prefix_gcs_uri: str,  # GoogleCloudStorageURI
    export_format: str = None,
) -> NamedTuple("Outputs", [
    ("model_dir_uri", str),  # GoogleCloudStorageURI
]):
    # Choose output_prefix_gcs_uri properly to avoid the following error:
    # google.api_core.exceptions.FailedPrecondition: 400 The Cloud Storage bucket of `gs://<output_prefix_gcs_uri>/model-7972079425934065664/tf-saved-model/2021-11-08T10:44:57.671790Z` is in location `us`.
    # It must be in the same regional location as the service location `us-central1`.
    from google.cloud import aiplatform

    model = aiplatform.Model(model_name=model_name)

    print("Available export formats:")
    print(model.supported_export_formats)
    if not export_format:
        export_format = list(model.supported_export_formats.keys())[0]
        print(f"Auto-selected export formats: {export_format}")

    result = model.export_model(
        export_format_id=export_format,
        artifact_destination=output_prefix_gcs_uri,
    )

    # == "gs://<artifact_destination>/model-7972079425934065664/tf-saved-model/2021-11-08T00:54:18.367871Z"
    artifact_output_uri = result["artifactOutputUri"]

    return (artifact_output_uri,)


if __name__ == "__main__":
    export_model_to_GCS_for_Google_Cloud_Vertex_AI_Model_op = create_component_from_func(
        export_model_to_GCS_for_Google_Cloud_Vertex_AI_Model,
        base_image="python:3.9",
        packages_to_install=["google-cloud-aiplatform==1.6.2"],
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Export/to_GCS/component.yaml",
        },
    )
