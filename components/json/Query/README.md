<!-- BEGIN_GENERATED_CONTENT -->
# Query JSON using JQ

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/json/Query/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Query/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Json** **\***||||
|**Query** **\***|[String]|||
|**Options** **\***|[String]|--raw-output||

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|||

## Implementation

#### Container

Container image: [stedolan/jq:latest](https://hub.docker.com/r/stedolan/jq)

## Usage

```python
query_JSON_using_JQ_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Query/component.yaml")
...
query_JSON_using_JQ_task = query_JSON_using_JQ_op(
    json=...,
    query=...,
    options=...,
)
```

## Other information

###### Tags

* input_type=[String]

[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
