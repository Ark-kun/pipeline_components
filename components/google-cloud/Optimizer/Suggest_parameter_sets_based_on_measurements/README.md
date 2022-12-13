<!-- BEGIN_GENERATED_CONTENT -->
# Suggest parameter sets from measurements using gcp ai platform optimizer

Description: Suggests trials (parameter sets) to evaluate.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Optimizer/Suggest_parameter_sets_based_on_measurements/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Optimizer/Suggest_parameter_sets_based_on_measurements/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**parameter_specs** **\***|[JsonArray]||List of parameter specs. See https://cloud.google.com/ai-platform/optimizer/docs/reference/rest/v1/projects.locations.studies#parameterspec|
|**metrics_for_parameter_sets** **\***|[JsonArray]||List of parameter sets and evaluation metrics for them. Each list item contains "parameters" dict and "metrics" dict. Example: {"parameters": {"p1": 1.1, "p2": 2.2}, "metrics": {"metric1": 101, "metric2": 102} }|
|**suggestion_count** **\***|[Integer]||Number of suggestions to request.|
|maximize|[Boolean]|False|Whether to miaximize or minimize when optimizing a single metric.Default is to minimize. Ignored if metric_specs list is provided.|
|metric_specs|[JsonArray]||List of metric specs. See https://cloud.google.com/ai-platform/optimizer/docs/reference/rest/v1/projects.locations.studies#metricspec|
|gcp_project_id|[String]|||
|gcp_region|[String]|us-central1||

## Outputs

|Name|Type|Description|
|-|-|-|
|suggested_parameter_sets|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.8](https://hub.docker.com/r/_/python)

## Usage

```python
suggest_parameter_sets_from_measurements_using_gcp_ai_platform_optimizer_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Optimizer/Suggest_parameter_sets_based_on_measurements/component.yaml")
...
suggest_parameter_sets_from_measurements_using_gcp_ai_platform_optimizer_task = suggest_parameter_sets_from_measurements_using_gcp_ai_platform_optimizer_op(
    parameter_specs=...,
    metrics_for_parameter_sets=...,
    suggestion_count=...,
    # Optional:
    # maximize=False,
    # metric_specs=[...],
    # gcp_project_id=...,
    # gcp_region="us-central1",
)
```

## Other information

###### Tags

* input_type=[Boolean]
* input_type=[Integer]
* input_type=[JsonArray]
* input_type=[String]
* output_type=[JsonArray]

[Boolean]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Boolean
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
