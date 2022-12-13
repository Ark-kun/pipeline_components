<!-- BEGIN_GENERATED_CONTENT -->
# SchemaGen

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/SchemaGen/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/SchemaGen/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**statistics** **\***|[ExampleStatistics]|||
|infer_feature_shape|[Integer]|||
|exclude_splits|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|schema|[Schema]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
schemaGen_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/SchemaGen/component.yaml")
...
schemaGen_task = schemaGen_op(
    statistics=...,
    # Optional:
    # infer_feature_shape=...,
    # exclude_splits=...,
)
```

## Other information

###### Tags

* input_type=[ExampleStatistics]
* input_type=[Integer]
* input_type=[String]
* output_type=[Schema]

[ExampleStatistics]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ExampleStatistics
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[Schema]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Schema
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
