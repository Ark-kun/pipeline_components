<!-- BEGIN_GENERATED_CONTENT -->
# Aggregate regression metrics

Description: Calculates regression metrics.

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/ml_metrics/Aggregate_regression_metrics/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ml_metrics/Aggregate_regression_metrics/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**metrics_1** **\***|[JsonObject]|||
|metrics_2|[JsonObject]|||
|metrics_3|[JsonObject]|||
|metrics_4|[JsonObject]|||
|metrics_5|[JsonObject]|||

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
aggregate_regression_metrics_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ml_metrics/Aggregate_regression_metrics/component.yaml")
...
aggregate_regression_metrics_task = aggregate_regression_metrics_op(
    metrics_1=...,
    # Optional:
    # metrics_2={...},
    # metrics_3={...},
    # metrics_4={...},
    # metrics_5={...},
)
```

## Other information

###### Tags

* input_type=[JsonObject]
* output_type=[Float]
* output_type=[Integer]
* output_type=[JsonObject]

[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
<!-- END_GENERATED_CONTENT -->
