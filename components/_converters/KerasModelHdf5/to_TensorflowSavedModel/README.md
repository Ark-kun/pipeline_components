<!-- BEGIN_GENERATED_CONTENT -->
# Keras convert hdf5 model to tf saved model

Description: Converts Keras HDF5 model to Tensorflow SavedModel format.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/KerasModelHdf5/to_TensorflowSavedModel/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/KerasModelHdf5/to_TensorflowSavedModel/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[KerasModelHdf5]||Keras model in HDF5 format.|

## Outputs

|Name|Type|Description|
|-|-|-|
|converted_model|[TensorflowSavedModel]|Keras model in Tensorflow SavedModel format.|

## Implementation

#### Container

Container image: [tensorflow/tensorflow:2.3.0](https://hub.docker.com/r/tensorflow/tensorflow)

## Usage

```python
keras_convert_hdf5_model_to_tf_saved_model_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/KerasModelHdf5/to_TensorflowSavedModel/component.yaml")
...
keras_convert_hdf5_model_to_tf_saved_model_task = keras_convert_hdf5_model_to_tf_saved_model_op(
    model=...,
)
```

## Other information

###### Tags

* input_type=[KerasModelHdf5]
* output_type=[TensorflowSavedModel]

[KerasModelHdf5]: https://github.com/Ark-kun/pipeline_components/tree/master/types/KerasModelHdf5
[TensorflowSavedModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TensorflowSavedModel
<!-- END_GENERATED_CONTENT -->
