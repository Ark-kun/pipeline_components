<!-- BEGIN_GENERATED_CONTENT -->
# Append boolean item to list

Description: Append item to a JSON array.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/List/Append/Boolean/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Append/Boolean/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**list** **\***|[JsonArray]|||
|**item** **\***|[Boolean]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
append_boolean_item_to_list_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Append/Boolean/component.yaml")
...
append_boolean_item_to_list_task = append_boolean_item_to_list_op(
    list=...,
    item=...,
)
```

## Other information

###### Tags

* input_type=[Boolean]
* input_type=[JsonArray]
* output_type=[JsonArray]

[Boolean]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Boolean
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
<!-- END_GENERATED_CONTENT -->
