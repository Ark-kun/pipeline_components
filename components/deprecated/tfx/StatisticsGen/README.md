<!-- BEGIN_GENERATED_CONTENT -->
# StatisticsGen

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/StatisticsGen/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/StatisticsGen/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**examples** **\***|[Examples]|||
|schema|[Schema]|||
|exclude_splits|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|statistics|[ExampleStatistics]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
statisticsGen_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/StatisticsGen/component.yaml")
...
statisticsGen_task = statisticsGen_op(
    examples=...,
    # Optional:
    # schema=...,
    # exclude_splits=...,
)
```

## Other information

###### Tags

* input_type=[Examples]
* input_type=[Schema]
* input_type=[String]
* output_type=[ExampleStatistics]

[ExampleStatistics]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ExampleStatistics
[Examples]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Examples
[Schema]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Schema
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
