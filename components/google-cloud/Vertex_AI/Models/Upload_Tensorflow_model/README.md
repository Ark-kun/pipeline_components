<!-- BEGIN_GENERATED_CONTENT -->
# Upload Tensorflow model to Google Cloud Vertex AI

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Vertex_AI/Models/Upload_Tensorflow_model/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Upload_Tensorflow_model/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[TensorflowSavedModel]|||
|tensorflow_version|[String]|||
|use_gpu|[Boolean]|False||
|display_name|[String]|||
|description|[String]|||
|project|[String]|||
|location|[String]|||
|labels|[JsonObject]|||
|staging_bucket|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|model_name|[GoogleCloudVertexAiModelName]||
|model_dict|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
upload_Tensorflow_model_to_Google_Cloud_Vertex_AI_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Upload_Tensorflow_model/component.yaml")
...
upload_Tensorflow_model_to_Google_Cloud_Vertex_AI_task = upload_Tensorflow_model_to_Google_Cloud_Vertex_AI_op(
    model=...,
    # Optional:
    # tensorflow_version=...,
    # use_gpu=False,
    # display_name=...,
    # description=...,
    # project=...,
    # location=...,
    # labels={...},
    # staging_bucket=...,
)
```

## Other information

###### Tags

* input_type=[Boolean]
* input_type=[JsonObject]
* input_type=[String]
* input_type=[TensorflowSavedModel]
* output_type=[GoogleCloudVertexAiModelName]
* output_type=[JsonObject]

[Boolean]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Boolean
[GoogleCloudVertexAiModelName]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GoogleCloudVertexAiModelName
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[TensorflowSavedModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TensorflowSavedModel
<!-- END_GENERATED_CONTENT -->
