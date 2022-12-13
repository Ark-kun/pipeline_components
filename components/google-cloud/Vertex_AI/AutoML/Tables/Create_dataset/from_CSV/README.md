<!-- BEGIN_GENERATED_CONTENT -->
# Create tabular dataset from CSV for Google Cloud Vertex AI

Description: Creates Google Cloud Vertex AI Tabular Dataset from CSV data stored in GCS.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Vertex_AI/AutoML/Tables/Create_dataset/from_GCS/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/AutoML/Tables/Create_dataset/from_GCS/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data** **\***|[CSV]||Data in CSV format that should be imported into the dataset.|
|display_name|[String]||Display name for the AutoML Dataset.<br/>Allowed characters are ASCII Latin letters A-Z and a-z, an underscore (_), and ASCII digits 0-9.|
|labels|[JsonObject]|||
|project|[String]||Google Cloud project ID. If not set, the default one will be used.|
|location|[String]|us-central1|Google Cloud region. AutoML Tables only supports us-central1.|
|encryption_spec_key_name|[String]|||
|staging_bucket|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|dataset_name|[GoogleCloudVertexAiTabularDatasetName]||
|dataset_dict|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
create_tabular_dataset_from_CSV_for_Google_Cloud_Vertex_AI_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/AutoML/Tables/Create_dataset/from_GCS/component.yaml")
...
create_tabular_dataset_from_CSV_for_Google_Cloud_Vertex_AI_task = create_tabular_dataset_from_CSV_for_Google_Cloud_Vertex_AI_op(
    data=...,
    # Optional:
    # display_name=...,
    # labels={...},
    # project=...,
    # location="us-central1",
    # encryption_spec_key_name=...,
    # staging_bucket=...,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[JsonObject]
* input_type=[String]
* output_type=[GoogleCloudVertexAiTabularDatasetName]
* output_type=[JsonObject]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[GoogleCloudVertexAiTabularDatasetName]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GoogleCloudVertexAiTabularDatasetName
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
