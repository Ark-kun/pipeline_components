<!-- BEGIN_GENERATED_CONTENT -->
# Get dict item from dict

Description: Gets item from a JSON array.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Dict/Get/Dict/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Get/Dict/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dict** **\***|[JsonObject]|||
|**key** **\***|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
get_dict_item_from_dict_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Get/Dict/component.yaml")
...
get_dict_item_from_dict_task = get_dict_item_from_dict_op(
    dict=...,
    key=...,
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
