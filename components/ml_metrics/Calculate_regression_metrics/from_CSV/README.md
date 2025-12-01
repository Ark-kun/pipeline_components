<!-- BEGIN_GENERATED_CONTENT -->
# Calculate regression metrics from CSV

Description: Calculates regression metrics.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**predictions** **\***|[CSV]|||
|label_column_name|[String]|label||
|prediction_column_name|[String]|prediction||

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

Container image: [python:3.12](https://hub.docker.com/r/_/python)

## Usage

```python
calculate_regression_metrics_from_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml")
...
calculate_regression_metrics_from_CSV_task = calculate_regression_metrics_from_CSV_op(
    predictions=...,
    # Optional:
    # label_column_name="label",
    # prediction_column_name="prediction",
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[String]
* output_type=[Float]
* output_type=[Integer]
* output_type=[JsonObject]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
