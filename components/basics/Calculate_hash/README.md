<!-- BEGIN_GENERATED_CONTENT -->
# Calculate data hash

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/basics/Calculate_hash/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/basics/Calculate_hash/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Data** **\***||||
|**Hash algorithm** **\***|[String]|SHA256|Hash algorithm to use. Supported values are MD5, SHA1, SHA256, SHA512, SHA3|

## Outputs

|Name|Type|Description|
|-|-|-|
|Hash|||

## Implementation

#### Container

Container image: [alpine](https://hub.docker.com/r/_/)

## Usage

```python
calculate_data_hash_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/basics/Calculate_hash/component.yaml")
...
calculate_data_hash_task = calculate_data_hash_op(
    data=...,
    hash_algorithm=...,
)
```

## Other information

###### Tags

* input_type=[String]

[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
