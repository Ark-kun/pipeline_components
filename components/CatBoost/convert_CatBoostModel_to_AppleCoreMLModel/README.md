<!-- BEGIN_GENERATED_CONTENT -->
# Convert CatBoostModel to AppleCoreMLModel

Description: Convert CatBoost model to Apple CoreML format.

    Args:
        model_path: Path of a trained model in binary CatBoost model format.
        converted_model_path: Output path for the converted model.

    Outputs:
        converted_model: Model in Apple CoreML format.

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/CatBoost/convert_CatBoostModel_to_AppleCoreMLModel/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/CatBoost/convert_CatBoostModel_to_AppleCoreMLModel/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[CatBoostModel]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|converted_model|[AppleCoreMLModel]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
convert_CatBoostModel_to_AppleCoreMLModel_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/CatBoost/convert_CatBoostModel_to_AppleCoreMLModel/component.yaml")
...
convert_CatBoostModel_to_AppleCoreMLModel_task = convert_CatBoostModel_to_AppleCoreMLModel_op(
    model=...,
)
```

## Other information

###### Tags

* input_type=[CatBoostModel]
* output_type=[AppleCoreMLModel]

[AppleCoreMLModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/AppleCoreMLModel
[CatBoostModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CatBoostModel
<!-- END_GENERATED_CONTENT -->
