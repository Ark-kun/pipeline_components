<!-- BEGIN_GENERATED_CONTENT -->
# Convert to OnnxModel from XGBoostJsonModel

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/OnnxModel/from_XGBoostJsonModel/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/OnnxModel/from_XGBoostJsonModel/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[XGBoostJsonModel]|||
|model_graph_name|[String]|||
|doc_string|[String]|||
|target_opset|[Integer]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|converted_model|[OnnxModel]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
convert_to_OnnxModel_from_XGBoostJsonModel_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/OnnxModel/from_XGBoostJsonModel/component.yaml")
...
convert_to_OnnxModel_from_XGBoostJsonModel_task = convert_to_OnnxModel_from_XGBoostJsonModel_op(
    model=...,
    # Optional:
    # model_graph_name=...,
    # doc_string=...,
    # target_opset=...,
)
```

## Other information

###### Tags

* input_type=[Integer]
* input_type=[String]
* input_type=[XGBoostJsonModel]
* output_type=[OnnxModel]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[OnnxModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/OnnxModel
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[XGBoostJsonModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/XGBoostJsonModel
<!-- END_GENERATED_CONTENT -->
