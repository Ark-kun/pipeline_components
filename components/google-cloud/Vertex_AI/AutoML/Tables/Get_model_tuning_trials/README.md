<!-- BEGIN_GENERATED_CONTENT -->
# Get model tuning trials for Google Cloud Vertex AI AutoML Tables

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Vertex_AI/AutoML/Tables/Get_model_tuning_trials/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/AutoML/Tables/Get_model_tuning_trials/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model_name** **\***|[GoogleCloudVertexAiModelName]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|tuning_trials|[JsonArray]||
|model_structures|[JsonArray]||
|extra_entries|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
get_model_tuning_trials_for_Google_Cloud_Vertex_AI_AutoML_Tables_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/AutoML/Tables/Get_model_tuning_trials/component.yaml")
...
get_model_tuning_trials_for_Google_Cloud_Vertex_AI_AutoML_Tables_task = get_model_tuning_trials_for_Google_Cloud_Vertex_AI_AutoML_Tables_op(
    model_name=...,
)
```

## Other information

###### Tags

* input_type=[GoogleCloudVertexAiModelName]
* output_type=[JsonArray]

[GoogleCloudVertexAiModelName]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GoogleCloudVertexAiModelName
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
<!-- END_GENERATED_CONTENT -->
