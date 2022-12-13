<!-- BEGIN_GENERATED_CONTENT -->
# ExampleValidator

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/ExampleValidator/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/ExampleValidator/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**statistics** **\***|[ExampleStatistics]|||
|**schema** **\***|[Schema]|||
|exclude_splits|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|anomalies|[ExampleAnomalies]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
exampleValidator_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/ExampleValidator/component.yaml")
...
exampleValidator_task = exampleValidator_op(
    statistics=...,
    schema=...,
    # Optional:
    # exclude_splits=...,
)
```

## Other information

###### Tags

* input_type=[ExampleStatistics]
* input_type=[Schema]
* input_type=[String]
* output_type=[ExampleAnomalies]

[ExampleAnomalies]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ExampleAnomalies
[ExampleStatistics]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ExampleStatistics
[Schema]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Schema
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
