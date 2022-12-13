<!-- BEGIN_GENERATED_CONTENT -->
# BigQueryExampleGen

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/ExampleGen/BigQueryExampleGen/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/ExampleGen/BigQueryExampleGen/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**input_config** **\***|[JsonObject]: `{"data_type": "proto:tfx.components.example_gen.Input"}`|||
|**output_config** **\***|[JsonObject]: `{"data_type": "proto:tfx.components.example_gen.Output"}`|||

## Outputs

|Name|Type|Description|
|-|-|-|
|examples|[Examples]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
bigQueryExampleGen_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/ExampleGen/BigQueryExampleGen/component.yaml")
...
bigQueryExampleGen_task = bigQueryExampleGen_op(
    input_config=...,
    output_config=...,
)
```

## Other information

###### Tags

* input_type=[JsonObject]
* output_type=[Examples]

[Examples]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Examples
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
<!-- END_GENERATED_CONTENT -->
