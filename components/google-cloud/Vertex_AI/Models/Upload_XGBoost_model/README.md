<!-- BEGIN_GENERATED_CONTENT -->
# Upload XGBoost model to Google Cloud Vertex AI

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Vertex_AI/Models/Upload_XGBoost_model/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Upload_XGBoost_model/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[XGBoostModel]|||
|xgboost_version|[String]|||
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
upload_XGBoost_model_to_Google_Cloud_Vertex_AI_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Upload_XGBoost_model/component.yaml")
...
upload_XGBoost_model_to_Google_Cloud_Vertex_AI_task = upload_XGBoost_model_to_Google_Cloud_Vertex_AI_op(
    model=...,
    # Optional:
    # xgboost_version=...,
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

* input_type=[JsonObject]
* input_type=[String]
* input_type=[XGBoostModel]
* output_type=[GoogleCloudVertexAiModelName]
* output_type=[JsonObject]

[GoogleCloudVertexAiModelName]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GoogleCloudVertexAiModelName
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[XGBoostModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/XGBoostModel
<!-- END_GENERATED_CONTENT -->
