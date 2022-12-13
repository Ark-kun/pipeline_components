<!-- BEGIN_GENERATED_CONTENT -->
# Build list of strings

Description: Creates a JSON array from multiple strings.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Build_list_of_strings/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Build_list_of_strings/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|item_1|[String]|||
|item_2|[String]|||
|item_3|[String]|||
|item_4|[String]|||
|item_5|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
build_list_of_strings_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Build_list_of_strings/component.yaml")
...
build_list_of_strings_task = build_list_of_strings_op(
    # Optional:
    # item_1=...,
    # item_2=...,
    # item_3=...,
    # item_4=...,
    # item_5=...,
)
```

## Other information

###### Tags

* input_type=[String]
* output_type=[JsonArray]

[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
