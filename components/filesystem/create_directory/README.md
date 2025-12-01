<!-- BEGIN_GENERATED_CONTENT -->
# Create directory from files (5)

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/filesystem/create_directory/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/filesystem/create_directory/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**File 1** **\***||||
|**File 1 name** **\***|[String]|1||
|File 2||||
|**File 2 name** **\***|[String]|2||
|File 3||||
|**File 3 name** **\***|[String]|3||
|File 4||||
|**File 4 name** **\***|[String]|4||
|File 5||||
|**File 5 name** **\***|[String]|5||

## Outputs

|Name|Type|Description|
|-|-|-|
|Directory|[Directory]||

## Implementation

#### Container

Container image: [alpine](https://hub.docker.com/r/_/)

## Usage

```python
create_directory_from_files_5_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/filesystem/create_directory/component.yaml")
...
create_directory_from_files_5_task = create_directory_from_files_5_op(
    file_1=...,
    file_1_name=...,
    file_2_name=...,
    file_3_name=...,
    file_4_name=...,
    file_5_name=...,
    # Optional:
    # file_2=...,
    # file_3=...,
    # file_4=...,
    # file_5=...,
)
```

## Other information

###### Tags

* input_type=[String]
* output_type=[Directory]

[Directory]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Directory
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
