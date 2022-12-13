<!-- BEGIN_GENERATED_CONTENT -->
# Set float item in dict

Description: Sets value for a key in a JSON object.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Dict/Set/Float/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Set/Float/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dict** **\***|[JsonObject]|||
|**key** **\***|[String]|||
|**value** **\***|[Float]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
set_float_item_in_dict_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Set/Float/component.yaml")
...
set_float_item_in_dict_task = set_float_item_in_dict_op(
    dict=...,
    key=...,
    value=...,
)
```

## Other information

###### Tags

* input_type=[Float]
* input_type=[JsonObject]
* input_type=[String]
* output_type=[JsonArray]

[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
