<!-- BEGIN_GENERATED_CONTENT -->
# Create dataset from CSV for Google Cloud AutoML Tables

Description: Creates Google Cloud AutoML Tables Dataset from CSV data.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/AutoML/Tables/Create_dataset/from_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/AutoML/Tables/Create_dataset/from_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data** **\***|[CSV]||Data in CSV format that will be imported to the dataset.|
|target_column_name|[String]||Name of the target column for training.|
|column_nullability|[JsonObject]|{}|Maps column name to boolean specifying whether the column should be marked as nullable.|
|column_types|[JsonObject]|{}|Maps column name to column type. Supported types: FLOAT64, CATEGORY, STRING.|
|gcs_staging_uri|[String]||URI of the data staging location in Google Cloud Storage. The bucket must have the us-central1 region. If not specified, a new staging bucket will be created.|
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

Container image: [python:3.8](https://hub.docker.com/r/_/python)

## Usage

```python
create_dataset_from_CSV_for_Google_Cloud_AutoML_Tables_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/AutoML/Tables/Create_dataset/from_CSV/component.yaml")
...
create_dataset_from_CSV_for_Google_Cloud_AutoML_Tables_task = create_dataset_from_CSV_for_Google_Cloud_AutoML_Tables_op(
    data=...,
    # Optional:
    # target_column_name=...,
    # column_nullability="{}",
    # column_types="{}",
    # gcs_staging_uri=...,
    # dataset_display_name=...,
    # gcp_project_id=...,
    # gcp_region="us-central1",
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[JsonObject]
* input_type=[String]
* output_type=[JsonObject]
* output_type=[String]
* output_type=[URI]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[URI]: https://github.com/Ark-kun/pipeline_components/tree/master/types/URI
<!-- END_GENERATED_CONTENT -->
