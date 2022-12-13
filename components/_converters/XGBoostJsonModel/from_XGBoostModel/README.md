<!-- BEGIN_GENERATED_CONTENT -->
# Convert to XGBoostJsonModel from XGBoostModel

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/XGBoostJsonModel/from_XGBoostModel/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/XGBoostJsonModel/from_XGBoostModel/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[XGBoostModel]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|converted_model|[XGBoostJsonModel]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
convert_to_XGBoostJsonModel_from_XGBoostModel_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/XGBoostJsonModel/from_XGBoostModel/component.yaml")
...
convert_to_XGBoostJsonModel_from_XGBoostModel_task = convert_to_XGBoostJsonModel_from_XGBoostModel_op(
    model=...,
)
```

## Other information

###### Tags

* input_type=[XGBoostModel]
* output_type=[XGBoostJsonModel]

[XGBoostJsonModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/XGBoostJsonModel
[XGBoostModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/XGBoostModel
<!-- END_GENERATED_CONTENT -->
