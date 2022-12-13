<!-- BEGIN_GENERATED_CONTENT -->
# SchemaGen

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/SchemaGen/with_URI_IO/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/SchemaGen/with_URI_IO/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**statistics_uri** **\***|[ExampleStatisticsUri]|||
|**output_schema_uri** **\***|[SchemaUri]|||
|infer_feature_shape|[Integer]|||
|exclude_splits|[String]|||
|beam_pipeline_args|[JsonArray]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|schema_uri|[SchemaUri]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
schemaGen_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/SchemaGen/with_URI_IO/component.yaml")
...
schemaGen_task = schemaGen_op(
    statistics_uri=...,
    output_schema_uri=...,
    # Optional:
    # infer_feature_shape=...,
    # exclude_splits=...,
    # beam_pipeline_args=[...],
)
```

## Other information

###### Tags

* input_type=[ExampleStatisticsUri]
* input_type=[Integer]
* input_type=[JsonArray]
* input_type=[SchemaUri]
* input_type=[String]
* output_type=[SchemaUri]

[ExampleStatisticsUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ExampleStatisticsUri
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[SchemaUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/SchemaUri
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
