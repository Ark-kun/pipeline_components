<!-- BEGIN_GENERATED_CONTENT -->
# Prepend float item to list

Description: Prepend item to a JSON array.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/List/Prepend/Float/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Prepend/Float/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**list** **\***|[JsonArray]|||
|**item** **\***|[Float]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
prepend_float_item_to_list_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Prepend/Float/component.yaml")
...
prepend_float_item_to_list_task = prepend_float_item_to_list_op(
    list=...,
    item=...,
)
```

## Other information

###### Tags

* input_type=[Float]
* input_type=[JsonArray]
* output_type=[JsonArray]

[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
<!-- END_GENERATED_CONTENT -->
