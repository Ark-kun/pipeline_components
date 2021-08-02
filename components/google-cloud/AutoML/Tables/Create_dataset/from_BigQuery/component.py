from typing import NamedTuple

from kfp.components import create_component_from_func

def create_dataset_from_BigQuery_for_Google_Cloud_AutoML_Tables(
    data_uri: 'GoogleCloudBigQueryUri',
    target_column_name: str = None,
    column_nullability: dict = {},
    column_types: dict = {},
    dataset_display_name: str = None,
    gcp_project_id: str = None,
    gcp_region: str = 'us-central1',  # Currently "us-central1" is the only region supported by AutoML tables.
) -> NamedTuple('Outputs', [
    ('dataset_name', str),
    ('dataset', dict),
    ('dataset_url', 'URI'),
]):
    '''Creates Google Cloud AutoML Tables Dataset from CSV data stored in GCS.

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

    Args:
        data_uri: Google Cloud BigQuery URI pointing to the data that should be imported into the dataset.
            The bucket must be a regional bucket in the us-central1 region.
            The file name must have a (case-insensitive) '.CSV' file extension.
        target_column_name: Name of the target column for training.
        column_nullability: Maps column name to boolean specifying whether the column should be marked as nullable.
        column_types: Maps column name to column type. Supported types: FLOAT64, CATEGORY, STRING.
        dataset_display_name: Display name for the AutoML Dataset.
            Allowed characters are ASCII Latin letters A-Z and a-z, an underscore (_), and ASCII digits 0-9.
        gcp_project_id: Google Cloud project ID. If not set, the default one will be used.
        gcp_region: Google Cloud region. AutoML Tables only supports us-central1.
    Returns:
        dataset_name: AutoML dataset name (fully-qualified)
    '''

    import datetime
    import logging

    import google.auth
    from google.cloud import automl_v1beta1 as automl
    from google.protobuf import json_format

    logging.getLogger().setLevel(logging.INFO)

    # Validating and inferring the arguments

    if not gcp_project_id:
        _, gcp_project_id = google.auth.default()

    if not gcp_region:
        gcp_region = 'us-central1'
    if gcp_region != 'us-central1':
        logging.warn('AutoML only supports the us-central1 region')
    if not dataset_display_name:
        dataset_display_name = 'Dataset_' + datetime.datetime.utcnow().strftime("%Y_%m_%d_%H_%M_%S")

    column_nullability = column_nullability or {}
    for name, nullability in column_nullability.items():
        assert isinstance(name, str)
        assert isinstance(nullability, bool)

    column_types = column_types or {}
    for name, data_type in column_types.items():
        assert isinstance(name, str)
        if not hasattr(automl.TypeCode, data_type):
            supported_types = [type_name for type_name in dir(automl.TypeCode) if type_name[0] != '_']
            raise ValueError(f'Unknown column type "{data_type}". Supported types: {supported_types}')

    logging.info(f'Creating AutoML Tables dataset.')
    automl_client = automl.AutoMlClient()

    project_location_path = f'projects/{gcp_project_id}/locations/{gcp_region}'

    dataset = automl.Dataset(
        display_name=dataset_display_name,
        tables_dataset_metadata=automl.TablesDatasetMetadata(),
        # labels={},
    )
    dataset = automl_client.create_dataset(
        dataset=dataset,
        parent=project_location_path,
    )
    dataset_id = dataset.name.split('/')[-1]
    dataset_web_url = f'https://console.cloud.google.com/automl-tables/locations/{gcp_region}/datasets/{dataset_id}'
    logging.info(f'Created dataset {dataset.name}.')
    logging.info(f'Link: {dataset_web_url}')

    logging.info(f'Importing data to the dataset: {dataset.name}.')
    import_data_input_config = automl.InputConfig(
        bigquery_source=automl.BigQuerySource(
            input_uri=data_uri,
        )
    )
    import_data_response = automl_client.import_data(
        name=dataset.name,
        input_config=import_data_input_config,
    )
    import_data_response.result()
    dataset = automl_client.get_dataset(
        name=dataset.name,
    )
    logging.info(f'Finished importing data.')

    logging.info('Updating column specs')
    target_column_spec = None
    primary_table_spec_name = dataset.name + '/tableSpecs/' + dataset.tables_dataset_metadata.primary_table_spec_id
    table_specs_list = list(automl_client.list_table_specs(
        parent=dataset.name,
    ))
    for table_spec in table_specs_list:
        column_specs_list = list(automl_client.list_column_specs(
            parent=table_spec.name,
        ))
        is_primary_table = table_spec.name == primary_table_spec_name
        for column_spec in column_specs_list:
            if column_spec.display_name == target_column_name and is_primary_table:
                target_column_spec = column_spec
            column_updated = False
            if column_spec.display_name in column_nullability:
                column_spec.data_type.nullable = column_nullability[column_spec.display_name]
                column_updated = True
            if column_spec.display_name in column_types:
                new_column_type = column_types[column_spec.display_name]
                column_spec.data_type.type_code = getattr(automl.TypeCode, new_column_type)
                column_updated = True
            if column_updated:
                automl_client.update_column_spec(column_spec=column_spec)

    if target_column_name:
        logging.info('Setting target column')
        if not target_column_spec:
            raise ValueError(f'Primary table does not have column "{target_column_name}"')
        target_column_spec_id = target_column_spec.name.split('/')[-1]
        dataset.tables_dataset_metadata.target_column_spec_id = target_column_spec_id
        dataset = automl_client.update_dataset(dataset=dataset)

    dataset_json = json_format.MessageToJson(dataset._pb)
    print(dataset_json)

    return (dataset.name, dataset_json, dataset_web_url)


if __name__ == '__main__':
    create_dataset_from_BigQuery_for_Google_Cloud_AutoML_Tables_op = create_component_from_func(
        create_dataset_from_BigQuery_for_Google_Cloud_AutoML_Tables,
        base_image='python:3.9',
        packages_to_install=['google-cloud-automl==2.4.2'],
        output_component_file='component.yaml',
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/AutoML/Tables/Create_dataset/from_BigQuery/component.yaml",
        },
    )
