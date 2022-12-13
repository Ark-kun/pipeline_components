<!-- BEGIN_GENERATED_CONTENT -->
# Convert Keras HDF5 model to Tensorflow JS GraphModel

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/TensorflowJSGraphModel/from_KerasModelHdf5/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/TensorflowJSGraphModel/from_KerasModelHdf5/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Model** **\***|[KerasModelHdf5]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Model|[TensorflowJSGraphModel]||

## Implementation

#### Container

Container image: [tensorflow/tensorflow:2.3.0](https://hub.docker.com/r/tensorflow/tensorflow)

## Usage

```python
convert_Keras_HDF5_model_to_Tensorflow_JS_GraphModel_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/TensorflowJSGraphModel/from_KerasModelHdf5/component.yaml")
...
convert_Keras_HDF5_model_to_Tensorflow_JS_GraphModel_task = convert_Keras_HDF5_model_to_Tensorflow_JS_GraphModel_op(
    model=...,
)
```

## Other information

###### Tags

* input_type=[KerasModelHdf5]
* output_type=[TensorflowJSGraphModel]

[KerasModelHdf5]: https://github.com/Ark-kun/pipeline_components/tree/master/types/KerasModelHdf5
[TensorflowJSGraphModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TensorflowJSGraphModel
<!-- END_GENERATED_CONTENT -->
