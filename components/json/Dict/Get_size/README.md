<!-- BEGIN_GENERATED_CONTENT -->
# Get size of dict

Description: Gets size of a JSON object.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Dict/Get_size/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Get_size/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dict** **\***|[JsonObject]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[Integer]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
get_size_of_dict_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Get_size/component.yaml")
...
get_size_of_dict_task = get_size_of_dict_op(
    dict=...,
)
```

## Other information

###### Tags

* input_type=[JsonObject]
* output_type=[Integer]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
<!-- END_GENERATED_CONTENT -->
