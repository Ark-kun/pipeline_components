<!-- BEGIN_GENERATED_CONTENT -->
# Filter text with pattern using JavaScript

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/sample/JavaScript/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/sample/JavaScript/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Text** **\***||||
|**Pattern** **\***|[String]|.*||

## Outputs

|Name|Type|Description|
|-|-|-|
|Filtered text|||

## Implementation

#### Container

Container image: [node:18.0.0-slim](https://hub.docker.com/r/_/node)

## Usage

```python
filter_text_with_pattern_using_JavaScript_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/sample/JavaScript/component.yaml")
...
filter_text_with_pattern_using_JavaScript_task = filter_text_with_pattern_using_JavaScript_op(
    text=...,
    pattern=...,
)
```

## Other information

###### Tags

* input_type=[String]

[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
