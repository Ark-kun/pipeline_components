<!-- BEGIN_GENERATED_CONTENT -->
# Convert Keras SavedModel to Tensorflow JS LayersModel

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/TensorflowJSLayersModel/from_TensorflowSavedModel/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/TensorflowJSLayersModel/from_TensorflowSavedModel/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Model** **\***|[TensorflowSavedModel]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Model|[TensorflowJSLayersModel]||

## Implementation

#### Container

Container image: [tensorflow/tensorflow:2.3.0](https://hub.docker.com/r/tensorflow/tensorflow)

## Usage

```python
convert_Keras_SavedModel_to_Tensorflow_JS_LayersModel_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/TensorflowJSLayersModel/from_TensorflowSavedModel/component.yaml")
...
convert_Keras_SavedModel_to_Tensorflow_JS_LayersModel_task = convert_Keras_SavedModel_to_Tensorflow_JS_LayersModel_op(
    model=...,
)
```

## Other information

###### Tags

* input_type=[TensorflowSavedModel]
* output_type=[TensorflowJSLayersModel]

[TensorflowJSLayersModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TensorflowJSLayersModel
[TensorflowSavedModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TensorflowSavedModel
<!-- END_GENERATED_CONTENT -->
