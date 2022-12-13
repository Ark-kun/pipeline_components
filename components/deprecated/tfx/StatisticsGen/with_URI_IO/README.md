<!-- BEGIN_GENERATED_CONTENT -->
# StatisticsGen

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/StatisticsGen/with_URI_IO/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/StatisticsGen/with_URI_IO/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**examples_uri** **\***|[ExamplesUri]|||
|**output_statistics_uri** **\***|[ExampleStatisticsUri]|||
|schema_uri|[SchemaUri]|||
|exclude_splits|[String]|||
|beam_pipeline_args|[JsonArray]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|statistics_uri|[ExampleStatisticsUri]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
statisticsGen_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/StatisticsGen/with_URI_IO/component.yaml")
...
statisticsGen_task = statisticsGen_op(
    examples_uri=...,
    output_statistics_uri=...,
    # Optional:
    # schema_uri=...,
    # exclude_splits=...,
    # beam_pipeline_args=[...],
)
```

## Other information

###### Tags

* input_type=[ExampleStatisticsUri]
* input_type=[ExamplesUri]
* input_type=[JsonArray]
* input_type=[SchemaUri]
* input_type=[String]
* output_type=[ExampleStatisticsUri]

[ExampleStatisticsUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ExampleStatisticsUri
[ExamplesUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ExamplesUri
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[SchemaUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/SchemaUri
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
