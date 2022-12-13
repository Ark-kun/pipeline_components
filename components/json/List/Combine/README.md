<!-- BEGIN_GENERATED_CONTENT -->
# Combine lists

Description: Combines multiple JSON arrays into one.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/List/Combine/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Combine/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|list_1|[JsonArray]|||
|list_2|[JsonArray]|||
|list_3|[JsonArray]|||
|list_4|[JsonArray]|||
|list_5|[JsonArray]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
combine_lists_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Combine/component.yaml")
...
combine_lists_task = combine_lists_op(
    # Optional:
    # list_1=[...],
    # list_2=[...],
    # list_3=[...],
    # list_4=[...],
    # list_5=[...],
)
```

## Other information

###### Tags

* input_type=[JsonArray]
* output_type=[JsonArray]

[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
<!-- END_GENERATED_CONTENT -->
