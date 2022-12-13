<!-- BEGIN_GENERATED_CONTENT -->
# Create list from dicts

Description: Creates a JSON array from JSON objects.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/List/Create/from_Dicts/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Create/from_Dicts/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|item_1|[JsonObject]|||
|item_2|[JsonObject]|||
|item_3|[JsonObject]|||
|item_4|[JsonObject]|||
|item_5|[JsonObject]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
create_list_from_dicts_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Create/from_Dicts/component.yaml")
...
create_list_from_dicts_task = create_list_from_dicts_op(
    # Optional:
    # item_1={...},
    # item_2={...},
    # item_3={...},
    # item_4={...},
    # item_5={...},
)
```

## Other information

###### Tags

* input_type=[JsonObject]
* output_type=[JsonArray]

[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
<!-- END_GENERATED_CONTENT -->
