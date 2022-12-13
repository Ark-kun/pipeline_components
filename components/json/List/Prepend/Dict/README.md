<!-- BEGIN_GENERATED_CONTENT -->
# Prepend dict item to list

Description: Prepend item to a JSON array.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/List/Prepend/Dict/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Prepend/Dict/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**list** **\***|[JsonArray]|||
|**item** **\***|[JsonObject]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
prepend_dict_item_to_list_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Prepend/Dict/component.yaml")
...
prepend_dict_item_to_list_task = prepend_dict_item_to_list_op(
    list=...,
    item=...,
)
```

## Other information

###### Tags

* input_type=[JsonArray]
* input_type=[JsonObject]
* output_type=[JsonArray]

[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
<!-- END_GENERATED_CONTENT -->
