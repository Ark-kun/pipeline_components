<!-- BEGIN_GENERATED_CONTENT -->
# Convert to OnnxModel from XGBoostModel

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/OnnxModel/from_XGBoostModel/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/OnnxModel/from_XGBoostModel/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[XGBoostModel]|||
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
convert_to_OnnxModel_from_XGBoostModel_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/OnnxModel/from_XGBoostModel/component.yaml")
...
convert_to_OnnxModel_from_XGBoostModel_task = convert_to_OnnxModel_from_XGBoostModel_op(
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
* input_type=[XGBoostModel]
* output_type=[OnnxModel]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[OnnxModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/OnnxModel
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[XGBoostModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/XGBoostModel
<!-- END_GENERATED_CONTENT -->
