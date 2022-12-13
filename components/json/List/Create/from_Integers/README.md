<!-- BEGIN_GENERATED_CONTENT -->
# Create list from integers

Description: Creates a JSON array from integers.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/List/Create/from_Integers/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Create/from_Integers/component.yaml)

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

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
create_list_from_integers_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Create/from_Integers/component.yaml")
...
create_list_from_integers_task = create_list_from_integers_op(
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
