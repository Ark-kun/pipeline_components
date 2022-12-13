<!-- BEGIN_GENERATED_CONTENT -->
# Create list from floats

Description: Creates a JSON array from floats.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/List/Create/from_Floats/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Create/from_Floats/component.yaml)

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

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
create_list_from_floats_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Create/from_Floats/component.yaml")
...
create_list_from_floats_task = create_list_from_floats_op(
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
