<!-- BEGIN_GENERATED_CONTENT -->
# Build list of integers

Description: Creates a JSON array from multiple integer numbers.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Build_list_of_integers/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Build_list_of_integers/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|item_1|[Integer]|||
|item_2|[Integer]|||
|item_3|[Integer]|||
|item_4|[Integer]|||
|item_5|[Integer]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.8](https://hub.docker.com/r/_/python)

## Usage

```python
build_list_of_integers_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Build_list_of_integers/component.yaml")
...
build_list_of_integers_task = build_list_of_integers_op(
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

* input_type=[Integer]
* output_type=[JsonArray]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
<!-- END_GENERATED_CONTENT -->
