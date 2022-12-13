<!-- BEGIN_GENERATED_CONTENT -->
# Convert to XGBoostModel from XGBoostJsonModel

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/XGBoostJsonModel/to_XGBoostModel/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/XGBoostJsonModel/to_XGBoostModel/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[XGBoostJsonModel]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|converted_model|[XGBoostModel]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
convert_to_XGBoostModel_from_XGBoostJsonModel_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/XGBoostJsonModel/to_XGBoostModel/component.yaml")
...
convert_to_XGBoostModel_from_XGBoostJsonModel_task = convert_to_XGBoostModel_from_XGBoostJsonModel_op(
    model=...,
)
```

## Other information

###### Tags

* input_type=[XGBoostJsonModel]
* output_type=[XGBoostModel]

[XGBoostJsonModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/XGBoostJsonModel
[XGBoostModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/XGBoostModel
<!-- END_GENERATED_CONTENT -->
