<!-- BEGIN_GENERATED_CONTENT -->
# Create tabular dataset from GCS for Google Cloud Vertex AI

Description: Creates Google Cloud Vertex AI Tabular Dataset from CSV data stored in GCS.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Vertex_AI/AutoML/Tables/Create_dataset/from_GCS/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/AutoML/Tables/Create_dataset/from_GCS/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data_uri** **\***|[GoogleCloudStorageUri]||Google Cloud Storage URI pointing to the data in CSV format that should be imported into the dataset.<br/>The bucket must be a regional bucket in the us-central1 region.<br/>The file name must have a (case-insensitive) '.CSV' file extension.|
|display_name|[String]||Display name for the AutoML Dataset.<br/>Allowed characters are ASCII Latin letters A-Z and a-z, an underscore (_), and ASCII digits 0-9.|
|encryption_spec_key_name|[String]||Optional. The Cloud KMS resource identifier of the customer<br/>managed encryption key used to protect a resource. Has the<br/>form:<br/>``projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key``.<br/>The key needs to be in the same region as where the compute<br/>resource is created.|
|project|[String]||Google Cloud project ID. If not set, the default one will be used.|
|location|[String]|us-central1|Google Cloud region. AutoML Tables only supports us-central1.|

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
create_tabular_dataset_from_GCS_for_Google_Cloud_Vertex_AI_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/AutoML/Tables/Create_dataset/from_GCS/component.yaml")
...
create_tabular_dataset_from_GCS_for_Google_Cloud_Vertex_AI_task = create_tabular_dataset_from_GCS_for_Google_Cloud_Vertex_AI_op(
    data_uri=...,
    # Optional:
    # display_name=...,
    # encryption_spec_key_name=...,
    # project=...,
    # location="us-central1",
)
```

## Other information

###### Tags

* input_type=[GoogleCloudStorageUri]
* input_type=[String]
* output_type=[GoogleCloudVertexAiTabularDatasetName]
* output_type=[JsonObject]

[GoogleCloudStorageUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GoogleCloudStorageUri
[GoogleCloudVertexAiTabularDatasetName]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GoogleCloudVertexAiTabularDatasetName
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
