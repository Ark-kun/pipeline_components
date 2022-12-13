<!-- BEGIN_GENERATED_CONTENT -->
# Get boolean item from list

Description: Gets item from a JSON array.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/List/Get/Boolean/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Get/Boolean/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**list** **\***|[JsonArray]|||
|**index** **\***|[Integer]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[Boolean]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
get_boolean_item_from_list_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Get/Boolean/component.yaml")
...
get_boolean_item_from_list_task = get_boolean_item_from_list_op(
    list=...,
    index=...,
)
```

## Other information

###### Tags

* input_type=[Integer]
* input_type=[JsonArray]
* output_type=[Boolean]

[Boolean]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Boolean
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
<!-- END_GENERATED_CONTENT -->
