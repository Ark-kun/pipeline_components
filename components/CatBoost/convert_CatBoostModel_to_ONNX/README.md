<!-- BEGIN_GENERATED_CONTENT -->
# Convert CatBoostModel to ONNX

Description: Convert CatBoost model to ONNX format.

    Args:
        model_path: Path of a trained model in binary CatBoost model format.
        converted_model_path: Output path for the converted model.

    Outputs:
        converted_model: Model in ONNX format.

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/CatBoost/convert_CatBoostModel_to_ONNX/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/CatBoost/convert_CatBoostModel_to_ONNX/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[CatBoostModel]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|converted_model|[ONNX]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
convert_CatBoostModel_to_ONNX_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/CatBoost/convert_CatBoostModel_to_ONNX/component.yaml")
...
convert_CatBoostModel_to_ONNX_task = convert_CatBoostModel_to_ONNX_op(
    model=...,
)
```

## Other information

###### Tags

* input_type=[CatBoostModel]
* output_type=[ONNX]

[CatBoostModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CatBoostModel
[ONNX]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ONNX
<!-- END_GENERATED_CONTENT -->
