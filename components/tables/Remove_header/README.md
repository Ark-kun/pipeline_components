<!-- BEGIN_GENERATED_CONTENT -->
# Remove header

Description: Remove the header line from CSV and TSV data (unconditionally)

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/tables/Remove_header/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/tables/Remove_header/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**table** **\***||||

## Outputs

|Name|Type|Description|
|-|-|-|
|table|||

## Implementation

#### Container

Container image: [alpine](https://hub.docker.com/r/_/)

## Usage

```python
remove_header_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/tables/Remove_header/component.yaml")
...
remove_header_task = remove_header_op(
    table=...,
)
```

## Other information

###### Tags

<!-- END_GENERATED_CONTENT -->
