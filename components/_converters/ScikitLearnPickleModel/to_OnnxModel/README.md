<!-- BEGIN_GENERATED_CONTENT -->
# Convert to OnnxModel from ScikitLearnPickleModel

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/ScikitLearnPickleModel/to_OnnxModel/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ScikitLearnPickleModel/to_OnnxModel/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[ScikitLearnPickleModel]|||
|doc_string|[String]|||
|target_opset|[Integer]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|converted_model|[OnnxModel]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
convert_to_OnnxModel_from_ScikitLearnPickleModel_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ScikitLearnPickleModel/to_OnnxModel/component.yaml")
...
convert_to_OnnxModel_from_ScikitLearnPickleModel_task = convert_to_OnnxModel_from_ScikitLearnPickleModel_op(
    model=...,
    # Optional:
    # doc_string=...,
    # target_opset=...,
)
```

## Other information

###### Tags

* input_type=[Integer]
* input_type=[ScikitLearnPickleModel]
* input_type=[String]
* output_type=[OnnxModel]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[OnnxModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/OnnxModel
[ScikitLearnPickleModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ScikitLearnPickleModel
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
