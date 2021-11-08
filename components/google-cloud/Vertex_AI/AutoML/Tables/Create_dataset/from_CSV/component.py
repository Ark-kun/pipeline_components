from typing import NamedTuple

from kfp.components import create_component_from_func, InputPath

def create_tabular_dataset_from_CSV_for_Google_Cloud_Vertex_AI(
    data_path: InputPath('CSV'),  # data_type: "CSV"
    display_name: str = None,
    labels: dict = None,
    project: str = None,
    location: str = 'us-central1',
    encryption_spec_key_name: str = None,
    staging_bucket: str = None,
) -> NamedTuple('Outputs', [
    ('dataset_name', 'GoogleCloudVertexAiTabularDatasetName'),
    ('dataset_dict', dict),
]):
    '''Creates Google Cloud Vertex AI Tabular Dataset from CSV data stored in GCS.

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

    Args:
        data_path: Data in CSV format that should be imported into the dataset.
        display_name: Display name for the AutoML Dataset.
            Allowed characters are ASCII Latin letters A-Z and a-z, an underscore (_), and ASCII digits 0-9.
        project: Google Cloud project ID. If not set, the default one will be used.
        location: Google Cloud region. AutoML Tables only supports us-central1.
    Returns:
        dataset_name: Dataset name (fully-qualified)
        dataset_dict: Dataset object in JSON format
    '''

    import datetime
    import json
    import logging
    import os
    import tempfile

    from google.cloud import aiplatform
    from google.cloud.aiplatform import utils as aiplatform_utils
    from google.protobuf import json_format

    logging.getLogger().setLevel(logging.INFO)

    if not display_name:
        display_name = 'Dataset_' + datetime.datetime.utcnow().strftime("%Y_%m_%d_%H_%M_%S")

    # Problem: Unlike KFP, when running on Vertex AI, google.auth.default() returns incorrect GCP project ID.
    # This leads to failure when trying to create any resource in the project.
    # google.api_core.exceptions.PermissionDenied: 403 Permission 'aiplatform.models.upload' denied on resource '//aiplatform.googleapis.com/projects/gbd40bc90c7804989-tp/locations/us-central1' (or it may not exist).
    # We can try and get the GCP project ID/number from the environment variables.
    if not project:
        project_number = os.environ.get("CLOUD_ML_PROJECT_ID")
        if project_number:
            print(f"Inferred project number: {project_number}")
            project = project_number
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
                    project = project_id
            except Exception as e:
                print(e)

    if not location:
        location = os.environ.get("CLOUD_ML_REGION")
    
    aiplatform.init(
        project=project,
        location=location,
        staging_bucket=staging_bucket,
        encryption_spec_key_name=encryption_spec_key_name,
    )
    
    # Stage the data
    # The file needs to have .CSV extension, so we need to rename or link it.
    staging_dir = tempfile.mkdtemp()
    staged_data_path = os.path.join(staging_dir, "dataset.csv")
    # Need to use symlink to prevent OSError: [Errno 18] Invalid cross-device link.
    os.symlink(src=data_path, dst=staged_data_path)
    staged_data_uri = aiplatform_utils.stage_local_data_in_gcs(data_path=staged_data_path)

    labels = labels or {}
    labels["component-source"] = "github-com-ark-kun-pipeline-components"

    # Create the dataset
    dataset = aiplatform.TabularDataset.create(
        display_name=display_name,
        gcs_source=staged_data_uri,
        labels=labels,
    )
    (_, dataset_project, _, dataset_location, _, dataset_id) = dataset.resource_name.split('/')
    dataset_web_url = f'https://console.cloud.google.com/vertex-ai/locations/{dataset_location}/datasets/{dataset_id}/analyze?project={dataset_project}'
    logging.info(f'Created dataset {dataset.name}.')
    logging.info(f'Link: {dataset_web_url}')
    dataset_json = json.dumps(dataset.to_dict(), indent=2)
    print(dataset_json)
    return (dataset.resource_name, dataset_json, dataset_web_url)


if __name__ == '__main__':
    create_tabular_dataset_from_CSV_for_Google_Cloud_Vertex_AI_op = create_component_from_func(
        create_tabular_dataset_from_CSV_for_Google_Cloud_Vertex_AI,
        base_image='python:3.9',
        packages_to_install=[
            # "google-cloud-aiplatform==1.6.2",
            "git+https://github.com/Ark-kun/python-aiplatform@8f61efb3a7903a6e0ef47d957f26ef3083581c7e#egg=google-cloud-aiplatform&subdirectory=.",  # branch: feat--Support-uploading-local-models
            "google-api-python-client==2.29.0",  # For project number -> project ID conversion
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/AutoML/Tables/Create_dataset/from_GCS/component.yaml",
        },
        output_component_file='component.yaml',
    )
