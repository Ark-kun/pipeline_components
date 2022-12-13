<!-- BEGIN_GENERATED_CONTENT -->
# Create Zip archive

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/basics/Create_Zip_archive/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/basics/Create_Zip_archive/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Data** **\***||||
|**Name** **\***|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Archive|[ZipArchive]||

## Implementation

#### Container

Container image: [joshkeegan/zip@sha256:e3c5e0cd05567f02e9ffd225029a7ecf8b13ccfa41cc5e2686f302f2fe7c5751](https://hub.docker.com/r/joshkeegan/zip@sha256)

## Usage

```python
create_Zip_archive_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/basics/Create_Zip_archive/component.yaml")
...
create_Zip_archive_task = create_Zip_archive_op(
    data=...,
    name=...,
)
```

## Other information

###### Tags

* input_type=[String]
* output_type=[ZipArchive]

[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[ZipArchive]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ZipArchive
<!-- END_GENERATED_CONTENT -->
