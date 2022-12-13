<!-- BEGIN_GENERATED_CONTENT -->
# Extract Zip archive

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/basics/Extract_Zip_archive/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/basics/Extract_Zip_archive/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Archive** **\***|[ZipArchive]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Data|[Directory]||

## Implementation

#### Container

Container image: [joshkeegan/zip@sha256:e3c5e0cd05567f02e9ffd225029a7ecf8b13ccfa41cc5e2686f302f2fe7c5751](https://hub.docker.com/r/joshkeegan/zip@sha256)

## Usage

```python
extract_Zip_archive_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/basics/Extract_Zip_archive/component.yaml")
...
extract_Zip_archive_task = extract_Zip_archive_op(
    archive=...,
)
```

## Other information

###### Tags

* input_type=[ZipArchive]
* output_type=[Directory]

[Directory]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Directory
[ZipArchive]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ZipArchive
<!-- END_GENERATED_CONTENT -->
