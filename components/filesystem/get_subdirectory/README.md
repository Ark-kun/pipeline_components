<!-- BEGIN_GENERATED_CONTENT -->
# Get subdirectory

Description: Get subdirectory from directory.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/filesystem/get_subdirectory/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/filesystem/get_subdirectory/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Directory** **\***|[Directory]|||
|**Subpath** **\***|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Subdir|[Directory]||

## Implementation

#### Container

Container image: [alpine](https://hub.docker.com/r/_/)

## Usage

```python
get_subdirectory_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/filesystem/get_subdirectory/component.yaml")
...
get_subdirectory_task = get_subdirectory_op(
    directory=...,
    subpath=...,
)
```

## Other information

###### Tags

* input_type=[Directory]
* input_type=[String]
* output_type=[Directory]

[Directory]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Directory
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
