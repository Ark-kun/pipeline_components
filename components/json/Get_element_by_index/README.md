<!-- BEGIN_GENERATED_CONTENT -->
# Get element by index from JSON

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Get_element_by_index/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Get_element_by_index/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Json** **\***||||
|**Index** **\***|[Integer]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|||

## Implementation

#### Container

Container image: [stedolan/jq:latest](https://hub.docker.com/r/stedolan/jq)

## Usage

```python
get_element_by_index_from_JSON_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Get_element_by_index/component.yaml")
...
get_element_by_index_from_JSON_task = get_element_by_index_from_JSON_op(
    json=...,
    index=...,
)
```

## Other information

###### Tags

* input_type=[Integer]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
<!-- END_GENERATED_CONTENT -->
