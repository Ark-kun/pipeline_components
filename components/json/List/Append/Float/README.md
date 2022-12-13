<!-- BEGIN_GENERATED_CONTENT -->
# Append float item to list

Description: Append item to a JSON array.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/List/Append/Float/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Append/Float/component.yaml)

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
append_float_item_to_list_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Append/Float/component.yaml")
...
append_float_item_to_list_task = append_float_item_to_list_op(
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
