from typing import NamedTuple


def create_dataset_for_google_cloud_automl_tables(
    display_name: str,
    description: str = None,
    tables_dataset_metadata: dict = {},
    gcp_project_id: str = None,
    gcp_region: str = None,
    retry_config: dict = None, # : google.api_core.retry.Retry = google.api_core.gapic_v1.method.DEFAULT,
    timeout: float = None, #=google.api_core.gapic_v1.method.DEFAULT,
) -> NamedTuple('Outputs', [
    ('dataset_name', str),
    ('dataset', dict), #data_type='GoogleCloudAutoMlDataset'
    ('dataset_path', str), # Deprecated
    ('create_time', str), # Deprecated
    ('dataset_id', str), # Deprecated
    ('dataset_url', 'URI')
]):
    '''Creates an empty Dataset for AutoML tables'''
    import logging
    import google
    from google.protobuf import json_format
    from google.cloud import automl_v1beta1 as automl
    client = automl.AutoMlClient()

    if not gcp_project_id:
        _, gcp_project_id = google.auth.default()

    if not gcp_region:
        gcp_region = 'us-central1'
    if gcp_region != 'us-central1':
        logging.warn('AutoML only supports the us-central1 region')

    dataset = client.create_dataset(
        parent=f"projects/{gcp_project_id}/locations/{gcp_region}",
        dataset=automl.Dataset(
            display_name=display_name,
            description=description,
            tables_dataset_metadata=tables_dataset_metadata,
        ),
        retry=google.api_core.retry.Retry(**retry_config) if retry_config else google.api_core.gapic_v1.method.DEFAULT,
        timeout=timeout or google.api_core.gapic_v1.method.DEFAULT,
        # ! metadata was dict before, but now it's a sequence of tuples.
        #metadata=(metadata or {}).items(),
    )
    dataset_json = json_format.MessageToJson(dataset._pb)
    print(dataset_json)
    dataset_id = dataset.name.rsplit('/', 1)[-1]
    dataset_url = f'https://console.cloud.google.com/automl-tables/locations/{gcp_region}/datasets/{dataset_id}/schemav2?project={gcp_project_id}'
    print(dataset_url)
    return (dataset.name, dataset_json, dataset.name, str(dataset.create_time), dataset_id, dataset_url)


if __name__ == '__main__':
    from kfp.components import create_component_from_func

    create_dataset_for_google_cloud_automl_tables_op = create_component_from_func(
        create_dataset_for_google_cloud_automl_tables,
        output_component_file='component.yaml',
        base_image='python:3.9',
        packages_to_install=['google-cloud-automl==2.4.2'],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/create_dataset_for_tables/component.yaml",
        },
    )
