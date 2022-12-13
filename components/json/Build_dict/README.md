<!-- BEGIN_GENERATED_CONTENT -->
# Build dict

Description: Creates a JSON object from multiple key and value pairs.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Build_dict/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Build_dict/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|key_1|[String]|||
|value_1|[JsonObject]|||
|key_2|[String]|||
|value_2|[JsonObject]|||
|key_3|[String]|||
|value_3|[JsonObject]|||
|key_4|[String]|||
|value_4|[JsonObject]|||
|key_5|[String]|||
|value_5|[JsonObject]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.8](https://hub.docker.com/r/_/python)

## Usage

```python
build_dict_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Build_dict/component.yaml")
...
build_dict_task = build_dict_op(
    # Optional:
    # key_1=...,
    # value_1={...},
    # key_2=...,
    # value_2={...},
    # key_3=...,
    # value_3={...},
    # key_4=...,
    # value_4={...},
    # key_5=...,
    # value_5={...},
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
