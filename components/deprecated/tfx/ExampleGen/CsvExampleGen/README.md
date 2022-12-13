<!-- BEGIN_GENERATED_CONTENT -->
# CsvExampleGen

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/ExampleGen/CsvExampleGen/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/ExampleGen/CsvExampleGen/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**input_base** **\***|[String]|||
|**input_config** **\***|[JsonObject]: `{"data_type": "proto:tfx.components.example_gen.Input"}`|||
|**output_config** **\***|[JsonObject]: `{"data_type": "proto:tfx.components.example_gen.Output"}`|||
|range_config|[JsonObject]: `{"data_type": "proto:tfx.configs.RangeConfig"}`|||

## Outputs

|Name|Type|Description|
|-|-|-|
|examples|[Examples]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
csvExampleGen_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/ExampleGen/CsvExampleGen/component.yaml")
...
csvExampleGen_task = csvExampleGen_op(
    input_base=...,
    input_config=...,
    output_config=...,
    # Optional:
    # range_config=...,
)
```

## Other information

###### Tags

* input_type=[JsonObject]
* input_type=[String]
* output_type=[Examples]

[Examples]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Examples
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
