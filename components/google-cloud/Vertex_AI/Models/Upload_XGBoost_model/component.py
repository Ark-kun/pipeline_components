from typing import NamedTuple

from kfp.components import create_component_from_func, InputPath, OutputPath


def upload_XGBoost_model_to_Google_Cloud_Vertex_AI(
    model_path: InputPath("XGBoostModel"),
    xgboost_version: str = None,

    display_name: str = None,
    description: str = None,

    # Uncomment when anyone requests these:
    # instance_schema_uri: str = None,
    # parameters_schema_uri: str = None,
    # prediction_schema_uri: str = None,
    # explanation_metadata: "google.cloud.aiplatform_v1.types.explanation_metadata.ExplanationMetadata" = None,
    # explanation_parameters: "google.cloud.aiplatform_v1.types.explanation.ExplanationParameters" = None,

    project: str = None,
    location: str = "us-central1",
    labels: dict = None,
    # encryption_spec_key_name: str = None,
    staging_bucket: str = None,
) -> NamedTuple("Outputs", [
    ("model_name", "GoogleCloudVertexAiModelName"),
    ("model_dict", dict),
]):
    kwargs = locals()
    kwargs.pop("model_path")

    import json
    import os
    from google.cloud import aiplatform

    # Problem: Unlike KFP, when running on Vertex AI, google.auth.default() returns incorrect GCP project ID.
    # This leads to failure when trying to create any resource in the project.
    # google.api_core.exceptions.PermissionDenied: 403 Permission 'aiplatform.models.upload' denied on resource '//aiplatform.googleapis.com/projects/gbd40bc90c7804989-tp/locations/us-central1' (or it may not exist).
    # We can try and get the GCP project ID/number from the environment variables.
    if not project:
        project_number = os.environ.get("CLOUD_ML_PROJECT_ID")
        if project_number:
            print(f"Inferred project number: {project_number}")
            kwargs["project"] = project_number
            # To improve the naming we try to convert the project number into the user project ID.
            try:
                from googleapiclient import discovery

                cloud_resource_manager_service = discovery.build(
                    "cloudresourcemanager", "v3"
                )
                project_id = (
                    cloud_resource_manager_service.projects()
                    .get(name=f"projects/{project_number}")
                    .execute()["projectId"]
                )
                if project_id:
                    print(f"Inferred project ID: {project_id}")
                    kwargs["project"] = project_id
            except Exception as e:
                print(e)

    if not location:
        kwargs["location"] = os.environ.get("CLOUD_ML_REGION")

    if not labels:
        kwargs["labels"] = {}
    kwargs["labels"]["component-source"] = "github-com-ark-kun-pipeline-components"

    model = aiplatform.Model.upload_xgboost_model_file(
        model_file_path=model_path,
        **kwargs,
    )
    model_json = json.dumps(model.to_dict(), indent=2)
    print(model_json)
    return (model.resource_name, model_json)


if __name__ == "__main__":
    # Getting input descriptions
    # try:
    #     from google.cloud import aiplatform
    #     upload_XGBoost_model_to_Google_Cloud_Vertex_AI.__doc__ = aiplatform.Model.upload_xgboost_model_file.__doc__
    # except ImportError:
    #     pass

    upload_XGBoost_model_to_Google_Cloud_Vertex_AI_op = create_component_from_func(
        func=upload_XGBoost_model_to_Google_Cloud_Vertex_AI,
        base_image="python:3.9",
        packages_to_install=[
            # "google-cloud-aiplatform==1.6.2",
            "git+https://github.com/Ark-kun/python-aiplatform@8f61efb3a7903a6e0ef47d957f26ef3083581c7e#egg=google-cloud-aiplatform&subdirectory=.",  # branch: feat--Support-uploading-local-models
            "google-api-python-client==2.29.0",  # For project number -> project ID conversion
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Upload_XGBoost_model/component.yaml",
        },
        output_component_file="component.yaml",
    )
