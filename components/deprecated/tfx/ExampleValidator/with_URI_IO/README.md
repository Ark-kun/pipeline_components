<!-- BEGIN_GENERATED_CONTENT -->
# ExampleValidator

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/ExampleValidator/with_URI_IO/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/ExampleValidator/with_URI_IO/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**statistics_uri** **\***|[ExampleStatisticsUri]|||
|**schema_uri** **\***|[SchemaUri]|||
|**output_anomalies_uri** **\***|[ExampleAnomaliesUri]|||
|exclude_splits|[String]|||
|beam_pipeline_args|[JsonArray]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|anomalies_uri|[ExampleAnomaliesUri]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
exampleValidator_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/ExampleValidator/with_URI_IO/component.yaml")
...
exampleValidator_task = exampleValidator_op(
    statistics_uri=...,
    schema_uri=...,
    output_anomalies_uri=...,
    # Optional:
    # exclude_splits=...,
    # beam_pipeline_args=[...],
)
```

## Other information

###### Tags

* input_type=[ExampleAnomaliesUri]
* input_type=[ExampleStatisticsUri]
* input_type=[JsonArray]
* input_type=[SchemaUri]
* input_type=[String]
* output_type=[ExampleAnomaliesUri]

[ExampleAnomaliesUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ExampleAnomaliesUri
[ExampleStatisticsUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ExampleStatisticsUri
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[SchemaUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/SchemaUri
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
