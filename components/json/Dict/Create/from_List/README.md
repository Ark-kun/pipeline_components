<!-- BEGIN_GENERATED_CONTENT -->
# Create dict from list value

Description: Creates a JSON object from key and value.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Dict/Create/from_List/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Create/from_List/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**key** **\***|[String]|||
|**value** **\***|[JsonArray]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
create_dict_from_list_value_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Create/from_List/component.yaml")
...
create_dict_from_list_value_task = create_dict_from_list_value_op(
    key=...,
    value=...,
)
```

## Other information

###### Tags

* input_type=[JsonArray]
* input_type=[String]
* output_type=[JsonObject]

[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
