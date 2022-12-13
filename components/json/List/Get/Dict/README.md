<!-- BEGIN_GENERATED_CONTENT -->
# Get dict item from list

Description: Gets item from a JSON array.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/List/Get/Dict/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Get/Dict/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**list** **\***|[JsonArray]|||
|**index** **\***|[Integer]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
get_dict_item_from_list_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Get/Dict/component.yaml")
...
get_dict_item_from_list_task = get_dict_item_from_list_op(
    list=...,
    index=...,
)
```

## Other information

###### Tags

* input_type=[Integer]
* input_type=[JsonArray]
* output_type=[JsonObject]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
<!-- END_GENERATED_CONTENT -->
