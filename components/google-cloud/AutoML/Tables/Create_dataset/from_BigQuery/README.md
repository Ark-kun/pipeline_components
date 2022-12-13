<!-- BEGIN_GENERATED_CONTENT -->
# Create dataset from BigQuery for Google Cloud AutoML Tables

Description: Creates Google Cloud AutoML Tables Dataset from CSV data stored in GCS.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/AutoML/Tables/Create_dataset/from_BigQuery/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/AutoML/Tables/Create_dataset/from_BigQuery/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data_uri** **\***|[GoogleCloudBigQueryUri]||Google Cloud BigQuery URI pointing to the data that should be imported into the dataset.<br/>The bucket must be a regional bucket in the us-central1 region.<br/>The file name must have a (case-insensitive) '.CSV' file extension.|
|target_column_name|[String]||Name of the target column for training.|
|column_nullability|[JsonObject]|{}|Maps column name to boolean specifying whether the column should be marked as nullable.|
|column_types|[JsonObject]|{}|Maps column name to column type. Supported types: FLOAT64, CATEGORY, STRING.|
|dataset_display_name|[String]||Display name for the AutoML Dataset.<br/>Allowed characters are ASCII Latin letters A-Z and a-z, an underscore (_), and ASCII digits 0-9.|
|gcp_project_id|[String]||Google Cloud project ID. If not set, the default one will be used.|
|gcp_region|[String]|us-central1|Google Cloud region. AutoML Tables only supports us-central1.|

## Outputs

|Name|Type|Description|
|-|-|-|
|dataset_name|[String]||
|dataset|[JsonObject]||
|dataset_url|[URI]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
create_dataset_from_BigQuery_for_Google_Cloud_AutoML_Tables_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/AutoML/Tables/Create_dataset/from_BigQuery/component.yaml")
...
create_dataset_from_BigQuery_for_Google_Cloud_AutoML_Tables_task = create_dataset_from_BigQuery_for_Google_Cloud_AutoML_Tables_op(
    data_uri=...,
    # Optional:
    # target_column_name=...,
    # column_nullability="{}",
    # column_types="{}",
    # dataset_display_name=...,
    # gcp_project_id=...,
    # gcp_region="us-central1",
)
```

## Other information

###### Tags

* input_type=[GoogleCloudBigQueryUri]
* input_type=[JsonObject]
* input_type=[String]
* output_type=[JsonObject]
* output_type=[String]
* output_type=[URI]

[GoogleCloudBigQueryUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GoogleCloudBigQueryUri
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[URI]: https://github.com/Ark-kun/pipeline_components/tree/master/types/URI
<!-- END_GENERATED_CONTENT -->
