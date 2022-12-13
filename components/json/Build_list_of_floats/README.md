<!-- BEGIN_GENERATED_CONTENT -->
# Build list of floats

Description: Creates a JSON array from multiple floating-point numbers.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Build_list_of_floats/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Build_list_of_floats/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|item_1|[Float]|||
|item_2|[Float]|||
|item_3|[Float]|||
|item_4|[Float]|||
|item_5|[Float]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.8](https://hub.docker.com/r/_/python)

## Usage

```python
build_list_of_floats_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Build_list_of_floats/component.yaml")
...
build_list_of_floats_task = build_list_of_floats_op(
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

* input_type=[Float]
* output_type=[JsonArray]

[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
<!-- END_GENERATED_CONTENT -->
