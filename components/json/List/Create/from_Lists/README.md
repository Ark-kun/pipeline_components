<!-- BEGIN_GENERATED_CONTENT -->
# Create list from lists

Description: Creates a JSON array from JSON arrays.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/List/Create/from_Lists/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Create/from_Lists/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|item_1|[JsonArray]|||
|item_2|[JsonArray]|||
|item_3|[JsonArray]|||
|item_4|[JsonArray]|||
|item_5|[JsonArray]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
create_list_from_lists_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Create/from_Lists/component.yaml")
...
create_list_from_lists_task = create_list_from_lists_op(
    # Optional:
    # item_1=[...],
    # item_2=[...],
    # item_3=[...],
    # item_4=[...],
    # item_5=[...],
)
```

## Other information

###### Tags

* input_type=[JsonArray]
* output_type=[JsonArray]

[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
<!-- END_GENERATED_CONTENT -->
