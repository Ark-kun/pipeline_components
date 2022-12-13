<!-- BEGIN_GENERATED_CONTENT -->
# Get boolean item from dict

Description: Gets item from a JSON array.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Dict/Get/Boolean/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Get/Boolean/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dict** **\***|[JsonObject]|||
|**key** **\***|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[Boolean]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
get_boolean_item_from_dict_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Get/Boolean/component.yaml")
...
get_boolean_item_from_dict_task = get_boolean_item_from_dict_op(
    dict=...,
    key=...,
)
```

## Other information

###### Tags

* input_type=[JsonObject]
* input_type=[String]
* output_type=[Boolean]

[Boolean]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Boolean
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
