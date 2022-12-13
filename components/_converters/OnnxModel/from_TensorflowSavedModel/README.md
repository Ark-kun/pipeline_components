<!-- BEGIN_GENERATED_CONTENT -->
# To ONNX from Tensorflow SavedModel

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/OnnxModel/from_TensorflowSavedModel/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/OnnxModel/from_TensorflowSavedModel/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Model** **\***|[TensorflowSavedModel]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Model|[OnnxModel]||

## Implementation

#### Container

Container image: [tensorflow/tensorflow:2.3.0](https://hub.docker.com/r/tensorflow/tensorflow)

## Usage

```python
to_ONNX_from_Tensorflow_SavedModel_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/OnnxModel/from_TensorflowSavedModel/component.yaml")
...
to_ONNX_from_Tensorflow_SavedModel_task = to_ONNX_from_Tensorflow_SavedModel_op(
    model=...,
)
```

## Other information

###### Tags

* input_type=[TensorflowSavedModel]
* output_type=[OnnxModel]

[OnnxModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/OnnxModel
[TensorflowSavedModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TensorflowSavedModel
<!-- END_GENERATED_CONTENT -->
