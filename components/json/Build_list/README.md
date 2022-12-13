<!-- BEGIN_GENERATED_CONTENT -->
# Build list

Description: Creates a JSON array from multiple items.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Build_list/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Build_list/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|item_1|[JsonObject]|||
|item_2|[JsonObject]|||
|item_3|[JsonObject]|||
|item_4|[JsonObject]|||
|item_5|[JsonObject]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.8](https://hub.docker.com/r/_/python)

## Usage

```python
build_list_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Build_list/component.yaml")
...
build_list_task = build_list_op(
    # Optional:
    # item_1={...},
    # item_2={...},
    # item_3={...},
    # item_4={...},
    # item_5={...},
)
```

## Other information

###### Tags

* input_type=[JsonObject]
* output_type=[JsonArray]

[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
<!-- END_GENERATED_CONTENT -->
