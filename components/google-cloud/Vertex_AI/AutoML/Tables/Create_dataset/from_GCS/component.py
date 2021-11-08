from typing import NamedTuple

from kfp.components import create_component_from_func

def create_tabular_dataset_from_GCS_for_Google_Cloud_Vertex_AI(
    data_uri: 'GoogleCloudStorageUri',  # data_type: "CSV"
    display_name: str = None,
    encryption_spec_key_name: str = None,
    project: str = None,
    location: str = 'us-central1',
) -> NamedTuple('Outputs', [
    ('dataset_name', 'GoogleCloudVertexAiTabularDatasetName'),
    ('dataset_dict', dict),
]):
    '''Creates Google Cloud Vertex AI Tabular Dataset from CSV data stored in GCS.

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

    Args:
        data_uri: Google Cloud Storage URI pointing to the data in CSV format that should be imported into the dataset.
            The bucket must be a regional bucket in the us-central1 region.
            The file name must have a (case-insensitive) '.CSV' file extension.
        display_name: Display name for the AutoML Dataset.
            Allowed characters are ASCII Latin letters A-Z and a-z, an underscore (_), and ASCII digits 0-9.
        encryption_spec_key_name (Optional[str]):
            Optional. The Cloud KMS resource identifier of the customer
            managed encryption key used to protect a resource. Has the
            form:
            ``projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key``.
            The key needs to be in the same region as where the compute
            resource is created.
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

    from google.cloud import aiplatform
    from google.protobuf import json_format

    logging.getLogger().setLevel(logging.INFO)

    if not display_name:
        display_name = 'Dataset_' + datetime.datetime.utcnow().strftime("%Y_%m_%d_%H_%M_%S")
    
    # Hack to enable passing multiple URIs
    # I could have created another component or added another input, but it seems to be too much hassle for now.
    # An alternative would have been to accept comma-delimited or semicolon-delimited URLs.
    if data_uri.startswith("["):
        data_uris = json.loads(data_uri)
    else:
        data_uris = [data_uri]

    # Problem: Unlike KFP, when running on Vertex AI, google.auth.default() returns incorrect GCP project ID.
    # This leads to failure when trying to create any resource in the project.
    # google.api_core.exceptions.PermissionDenied: 403 Permission 'aiplatform.models.upload' denied on resource '//aiplatform.googleapis.com/projects/gbd40bc90c7804989-tp/locations/us-central1' (or it may not exist).
    # We can try and get the GCP project ID/number from the environment variables.
    if not project:
        project_number = os.environ.get("CLOUD_ML_PROJECT_ID")
        if project_number:
            print(f"Inferred project number: {project_number}")
            project = project_number

    if not location:
        location = os.environ.get("CLOUD_ML_REGION")

    aiplatform.init(
        project=project,
        location=location,
        encryption_spec_key_name=encryption_spec_key_name,
    )
    dataset = aiplatform.TabularDataset.create(
        display_name=display_name,
        gcs_source=data_uris,
    )
    (_, dataset_project, _, dataset_location, _, dataset_id) = dataset.resource_name.split('/')
    dataset_web_url = f'https://console.cloud.google.com/vertex-ai/locations/{dataset_location}/datasets/{dataset_id}/analyze?project={dataset_project}'
    logging.info(f'Created dataset {dataset.name}.')
    logging.info(f'Link: {dataset_web_url}')
    dataset_json = json_format.MessageToJson(dataset._gca_resource._pb)
    print(dataset_json)
    return (dataset.resource_name, dataset_json, dataset_web_url)


if __name__ == '__main__':
    create_tabular_dataset_from_GCS_for_Google_Cloud_Vertex_AI_op = create_component_from_func(
        create_tabular_dataset_from_GCS_for_Google_Cloud_Vertex_AI,
        base_image='python:3.9',
        packages_to_install=['google-cloud-aiplatform==1.1.1'],
        output_component_file='component.yaml',
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/AutoML/Tables/Create_dataset/from_GCS/component.yaml",
        },
    )
