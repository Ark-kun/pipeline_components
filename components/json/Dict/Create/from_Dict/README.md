<!-- BEGIN_GENERATED_CONTENT -->
# Create dict from dict value Train model using Keras on CSV

Description: Creates a JSON object from key and value.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Dict/Create/from_Dict/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Create/from_Dict/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**key** **\***|[String]|||
|**value** **\***|[JsonObject]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
create_dict_from_dict_value_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Create/from_Dict/component.yaml")
...
create_dict_from_dict_value_task = create_dict_from_dict_value_op(
    key=...,
    value=...,
)
```

## Other information

###### Tags

* input_type=[JsonObject]
* input_type=[String]
* output_type=[JsonObject]

[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->