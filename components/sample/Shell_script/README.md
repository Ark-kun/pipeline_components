<!-- BEGIN_GENERATED_CONTENT -->
# Filter text using shell and grep

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/sample/Shell_script/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/sample/Shell_script/component.yaml)

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

Container image: [alpine](https://hub.docker.com/r/_/)

## Usage

```python
filter_text_using_shell_and_grep_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/sample/Shell_script/component.yaml")
...
filter_text_using_shell_and_grep_task = filter_text_using_shell_and_grep_op(
    text=...,
    pattern=...,
)
```

## Other information

###### Tags

<!-- END_GENERATED_CONTENT -->
