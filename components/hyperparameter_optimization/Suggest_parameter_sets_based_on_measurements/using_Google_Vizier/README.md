<!-- BEGIN_GENERATED_CONTENT -->
# Suggest parameter sets based on measurements using google vizier

Description: Suggests parameter sets to evaluate based on the past measurements.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/hyperparameter_optimization/Suggest_parameter_sets_based_on_measurements/using_Google_Vizier/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/hyperparameter_optimization/Suggest_parameter_sets_based_on_measurements/using_Google_Vizier/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**parameter_specs** **\***|[JsonArray]||List of parameter specs. See https://github.com/google/vizier/blob/e92ab53bce139c89aff8c1590122c6b22adb5f47/vizier/service/study.proto#L171|
|**metrics_for_parameter_sets** **\***|[JsonArray]||List of parameter sets and evaluation metrics for them.<br/>Each list item contains "parameters" dict and "metrics" dict.<br/>Example: [{"parameters": {"p1": 1.1, "p2": 2.2}, "metrics": {"metric1": 101, "metric2": 102}}]|
|**suggestion_count** **\***|[Integer]||Number of suggestions to request.|
|algorithm|[String]|GRID_SEARCH|The suggestion algorithm to use.<br/>Supported values: RANDOM_SEARCH, QUASI_RANDOM_SEARCH, GRID_SEARCH, NSGA2, EMUKIT_GP_EI, BOCS, HARMONICA, CMA_ES.<br/>See https://github.com/google/vizier/blob/4d4c3c517316c9650ad6e45dce0985fc609357e9/vizier/_src/pyvizier/oss/study_config.py#L45|
|algorithm_config|[JsonObject]||Configuration of the chosen algorithm (as a dictionary).|
|maximize|[Boolean]|False|Whether to miaximize or minimize when optimizing a single metric. Default is to minimize. Ignored if metric_specs list is provided.|
|metric_specs|[JsonArray]||List of metric specs. See https://github.com/google/vizier/blob/e92ab53bce139c89aff8c1590122c6b22adb5f47/vizier/service/study.proto#L150|

## Outputs

|Name|Type|Description|
|-|-|-|
|suggested_parameter_sets|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
suggest_parameter_sets_based_on_measurements_using_google_vizier_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/hyperparameter_optimization/Suggest_parameter_sets_based_on_measurements/using_Google_Vizier/component.yaml")
...
suggest_parameter_sets_based_on_measurements_using_google_vizier_task = suggest_parameter_sets_based_on_measurements_using_google_vizier_op(
    parameter_specs=...,
    metrics_for_parameter_sets=...,
    suggestion_count=...,
    # Optional:
    # algorithm="GRID_SEARCH",
    # algorithm_config={...},
    # maximize=False,
    # metric_specs=[...],
)
```

## Other information

###### Tags

* input_type=[Boolean]
* input_type=[Integer]
* input_type=[JsonArray]
* input_type=[JsonObject]
* input_type=[String]
* output_type=[JsonArray]

[Boolean]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Boolean
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
