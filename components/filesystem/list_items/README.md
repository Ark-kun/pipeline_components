<!-- BEGIN_GENERATED_CONTENT -->
# List items

Description: Recursively list directory contents.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/filesystem/list_items/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/filesystem/list_items/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Directory** **\***|[Directory]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Items|||

## Implementation

#### Container

Container image: [alpine](https://hub.docker.com/r/_/)

## Usage

```python
list_items_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/filesystem/list_items/component.yaml")
...
list_items_task = list_items_op(
    directory=...,
)
```

## Other information

###### Tags

* input_type=[Directory]

[Directory]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Directory
<!-- END_GENERATED_CONTENT -->
