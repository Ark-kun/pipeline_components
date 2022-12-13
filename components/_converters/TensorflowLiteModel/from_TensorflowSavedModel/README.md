<!-- BEGIN_GENERATED_CONTENT -->
# Convert Tensorflow SavedModel to Tensorflow Lite model

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/TensorflowLiteModel/from_TensorflowSavedModel/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/TensorflowLiteModel/from_TensorflowSavedModel/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Model** **\***|[TensorflowSavedModel]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Model|[TensorflowLiteModel]||

## Implementation

#### Container

Container image: [tensorflow/tensorflow:2.3.0](https://hub.docker.com/r/tensorflow/tensorflow)

## Usage

```python
convert_Tensorflow_SavedModel_to_Tensorflow_Lite_model_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/TensorflowLiteModel/from_TensorflowSavedModel/component.yaml")
...
convert_Tensorflow_SavedModel_to_Tensorflow_Lite_model_task = convert_Tensorflow_SavedModel_to_Tensorflow_Lite_model_op(
    model=...,
)
```

## Other information

###### Tags

* input_type=[TensorflowSavedModel]
* output_type=[TensorflowLiteModel]

[TensorflowLiteModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TensorflowLiteModel
[TensorflowSavedModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TensorflowSavedModel
<!-- END_GENERATED_CONTENT -->
