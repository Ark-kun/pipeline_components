<!-- BEGIN_GENERATED_CONTENT -->
# Upload PyTorch model archive to Google Cloud Vertex AI

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Vertex_AI/Models/Upload_PyTorch_model_archive/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Upload_PyTorch_model_archive/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model_archive** **\***|[PyTorchModelArchive]|||
|torchserve_version|[String]|0.6.0||
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
upload_PyTorch_model_archive_to_Google_Cloud_Vertex_AI_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Upload_PyTorch_model_archive/component.yaml")
...
upload_PyTorch_model_archive_to_Google_Cloud_Vertex_AI_task = upload_PyTorch_model_archive_to_Google_Cloud_Vertex_AI_op(
    model_archive=...,
    # Optional:
    # torchserve_version="0.6.0",
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
* input_type=[PyTorchModelArchive]
* input_type=[String]
* output_type=[GoogleCloudVertexAiModelName]
* output_type=[JsonObject]

[Boolean]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Boolean
[GoogleCloudVertexAiModelName]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GoogleCloudVertexAiModelName
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[PyTorchModelArchive]: https://github.com/Ark-kun/pipeline_components/tree/master/types/PyTorchModelArchive
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
