<!-- BEGIN_GENERATED_CONTENT -->
# Calculate regression metrics from split text files

Description: Calculates regression metrics.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/ml_metrics/Calculate_regression_metrics/from_split_text_files/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ml_metrics/Calculate_regression_metrics/from_split_text_files/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**true_values** **\***||||
|**predicted_values** **\***||||

## Outputs

|Name|Type|Description|
|-|-|-|
|number_of_items|[Integer]||
|max_absolute_error|[Float]||
|mean_absolute_error|[Float]||
|mean_squared_error|[Float]||
|root_mean_squared_error|[Float]||
|metrics|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
calculate_regression_metrics_from_split_text_files_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ml_metrics/Calculate_regression_metrics/from_split_text_files/component.yaml")
...
calculate_regression_metrics_from_split_text_files_task = calculate_regression_metrics_from_split_text_files_op(
    true_values=...,
    predicted_values=...,
)
```

## Other information

###### Tags

* output_type=[Float]
* output_type=[Integer]
* output_type=[JsonObject]

[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
<!-- END_GENERATED_CONTENT -->
