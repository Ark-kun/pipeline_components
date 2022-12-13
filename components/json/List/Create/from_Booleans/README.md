<!-- BEGIN_GENERATED_CONTENT -->
# Create list from booleans

Description: Creates a JSON array from booleans.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/List/Create/from_Booleans/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Create/from_Booleans/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|item_1|[Boolean]|||
|item_2|[Boolean]|||
|item_3|[Boolean]|||
|item_4|[Boolean]|||
|item_5|[Boolean]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
create_list_from_booleans_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Create/from_Booleans/component.yaml")
...
create_list_from_booleans_task = create_list_from_booleans_op(
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

* input_type=[Boolean]
* output_type=[JsonArray]

[Boolean]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Boolean
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
<!-- END_GENERATED_CONTENT -->
