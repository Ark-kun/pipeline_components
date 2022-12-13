<!-- BEGIN_GENERATED_CONTENT -->
# Upload Scikit learn pickle model to Google Cloud Vertex AI

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Vertex_AI/Models/Upload_Scikit-learn_pickle_model/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Upload_Scikit-learn_pickle_model/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[ScikitLearnPickleModel]|||
|sklearn_version|[String]|||
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
upload_Scikit_learn_pickle_model_to_Google_Cloud_Vertex_AI_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Upload_Scikit-learn_pickle_model/component.yaml")
...
upload_Scikit_learn_pickle_model_to_Google_Cloud_Vertex_AI_task = upload_Scikit_learn_pickle_model_to_Google_Cloud_Vertex_AI_op(
    model=...,
    # Optional:
    # sklearn_version=...,
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
* input_type=[ScikitLearnPickleModel]
* input_type=[String]
* output_type=[GoogleCloudVertexAiModelName]
* output_type=[JsonObject]

[GoogleCloudVertexAiModelName]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GoogleCloudVertexAiModelName
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[ScikitLearnPickleModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ScikitLearnPickleModel
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
