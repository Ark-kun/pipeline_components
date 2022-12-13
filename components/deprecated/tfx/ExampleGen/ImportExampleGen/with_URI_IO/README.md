<!-- BEGIN_GENERATED_CONTENT -->
# ImportExampleGen

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/ExampleGen/ImportExampleGen/with_URI_IO/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/ExampleGen/ImportExampleGen/with_URI_IO/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**output_examples_uri** **\***|[ExamplesUri]|||
|**input_base** **\***|[String]|||
|**input_config** **\***|[JsonObject]: `{"data_type": "proto:tfx.components.example_gen.Input"}`|||
|**output_config** **\***|[JsonObject]: `{"data_type": "proto:tfx.components.example_gen.Output"}`|||
|range_config|[JsonObject]: `{"data_type": "proto:tfx.configs.RangeConfig"}`|||
|beam_pipeline_args|[JsonArray]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|examples_uri|[ExamplesUri]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
importExampleGen_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/ExampleGen/ImportExampleGen/with_URI_IO/component.yaml")
...
importExampleGen_task = importExampleGen_op(
    output_examples_uri=...,
    input_base=...,
    input_config=...,
    output_config=...,
    # Optional:
    # range_config=...,
    # beam_pipeline_args=[...],
)
```

## Other information

###### Tags

* input_type=[ExamplesUri]
* input_type=[JsonArray]
* input_type=[JsonObject]
* input_type=[String]
* output_type=[ExamplesUri]

[ExamplesUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ExamplesUri
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
