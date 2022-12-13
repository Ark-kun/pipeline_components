<!-- BEGIN_GENERATED_CONTENT -->
# Filter text

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/sample/R_script/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/sample/R_script/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Text** **\***||||
|**Pattern** **\***||.*||

## Outputs

|Name|Type|Description|
|-|-|-|
|Filtered text|||

## Implementation

#### Container

Container image: [r-base:4.0.2](https://hub.docker.com/r/_/r-base)

## Usage

```python
filter_text_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/sample/R_script/component.yaml")
...
filter_text_task = filter_text_op(
    text=...,
    pattern=...,
)
```

## Other information

###### Tags

<!-- END_GENERATED_CONTENT -->
