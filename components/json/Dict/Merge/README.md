<!-- BEGIN_GENERATED_CONTENT -->
# Merge dicts

Description: Merges multiple JSON objects into one.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Dict/Merge/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Merge/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|dict_1|[JsonObject]|||
|dict_2|[JsonObject]|||
|dict_3|[JsonObject]|||
|dict_4|[JsonObject]|||
|dict_5|[JsonObject]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
merge_dicts_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Merge/component.yaml")
...
merge_dicts_task = merge_dicts_op(
    # Optional:
    # dict_1={...},
    # dict_2={...},
    # dict_3={...},
    # dict_4={...},
    # dict_5={...},
)
```

## Other information

###### Tags

* input_type=[JsonObject]
* output_type=[JsonObject]

[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
<!-- END_GENERATED_CONTENT -->
