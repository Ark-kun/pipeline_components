<!-- BEGIN_GENERATED_CONTENT -->
# Suggest trials in gcp ai platform optimizer

Description: Suggests trials (parameter sets) to evaluate.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Optimizer/Suggest_trials/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Optimizer/Suggest_trials/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**study_name** **\***|[String]||Full resource name of the study.|
|**suggestion_count** **\***|[Integer]||Number of suggestions to request.|
|gcp_project_id|[String]|||
|gcp_region|[String]|us-central1||

## Outputs

|Name|Type|Description|
|-|-|-|
|suggested_trials|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.8](https://hub.docker.com/r/_/python)

## Usage

```python
suggest_trials_in_gcp_ai_platform_optimizer_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Optimizer/Suggest_trials/component.yaml")
...
suggest_trials_in_gcp_ai_platform_optimizer_task = suggest_trials_in_gcp_ai_platform_optimizer_op(
    study_name=...,
    suggestion_count=...,
    # Optional:
    # gcp_project_id=...,
    # gcp_region="us-central1",
)
```

## Other information

###### Tags

* input_type=[Integer]
* input_type=[String]
* output_type=[JsonArray]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
