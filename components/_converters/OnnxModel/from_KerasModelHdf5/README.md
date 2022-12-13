<!-- BEGIN_GENERATED_CONTENT -->
# To ONNX from Keras HDF5 model

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/OnnxModel/from_KerasModelHdf5/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/OnnxModel/from_KerasModelHdf5/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Model** **\***|[KerasModelHdf5]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Model|[OnnxModel]||

## Implementation

#### Container

Container image: [tensorflow/tensorflow:2.3.0](https://hub.docker.com/r/tensorflow/tensorflow)

## Usage

```python
to_ONNX_from_Keras_HDF5_model_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/OnnxModel/from_KerasModelHdf5/component.yaml")
...
to_ONNX_from_Keras_HDF5_model_task = to_ONNX_from_Keras_HDF5_model_op(
    model=...,
)
```

## Other information

###### Tags

* input_type=[KerasModelHdf5]
* output_type=[OnnxModel]

[KerasModelHdf5]: https://github.com/Ark-kun/pipeline_components/tree/master/types/KerasModelHdf5
[OnnxModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/OnnxModel
<!-- END_GENERATED_CONTENT -->
