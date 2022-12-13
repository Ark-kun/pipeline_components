<!-- BEGIN_GENERATED_CONTENT -->
# Export model to GCS for Google Cloud Vertex AI Model

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Vertex_AI/Models/Export/to_GCS/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Export/to_GCS/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model_name** **\***|[GoogleCloudVertexAiModelName]|||
|**output_prefix_gcs_uri** **\***|[String]|||
|export_format|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|model_dir_uri|[String]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
export_model_to_GCS_for_Google_Cloud_Vertex_AI_Model_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Export/to_GCS/component.yaml")
...
export_model_to_GCS_for_Google_Cloud_Vertex_AI_Model_task = export_model_to_GCS_for_Google_Cloud_Vertex_AI_Model_op(
    model_name=...,
    output_prefix_gcs_uri=...,
    # Optional:
    # export_format=...,
)
```

## Other information

###### Tags

* input_type=[GoogleCloudVertexAiModelName]
* input_type=[String]
* output_type=[String]

[GoogleCloudVertexAiModelName]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GoogleCloudVertexAiModelName
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
