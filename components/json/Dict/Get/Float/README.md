<!-- BEGIN_GENERATED_CONTENT -->
# Get float item from dict

Description: Gets item from a JSON array.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Dict/Get/Float/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Get/Float/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dict** **\***|[JsonObject]|||
|**key** **\***|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[Float]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
get_float_item_from_dict_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Get/Float/component.yaml")
...
get_float_item_from_dict_task = get_float_item_from_dict_op(
    dict=...,
    key=...,
)
```

## Other information

###### Tags

* input_type=[JsonObject]
* input_type=[String]
* output_type=[Float]

[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
