<!-- BEGIN_GENERATED_CONTENT -->
# Convert to TensorflowSavedModel from OnnxModel

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/OnnxModel/to_TensorflowSavedModel/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/OnnxModel/to_TensorflowSavedModel/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[OnnxModel]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|converted_model|[TensorflowSavedModel]||

## Implementation

#### Container

Container image: [tensorflow/tensorflow:2.8.0](https://hub.docker.com/r/tensorflow/tensorflow)

## Usage

```python
convert_to_TensorflowSavedModel_from_OnnxModel_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/OnnxModel/to_TensorflowSavedModel/component.yaml")
...
convert_to_TensorflowSavedModel_from_OnnxModel_task = convert_to_TensorflowSavedModel_from_OnnxModel_op(
    model=...,
)
```

## Other information

###### Tags

* input_type=[OnnxModel]
* output_type=[TensorflowSavedModel]

[OnnxModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/OnnxModel
[TensorflowSavedModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TensorflowSavedModel
<!-- END_GENERATED_CONTENT -->
