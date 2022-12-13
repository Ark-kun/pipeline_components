<!-- BEGIN_GENERATED_CONTENT -->
# Download from GCS

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/storage/download/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/storage/download/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**GCS path** **\***|[URI]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Data|||

## Implementation

#### Container

Container image: [google/cloud-sdk](https://hub.docker.com/r/)

## Usage

```python
download_from_GCS_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/storage/download/component.yaml")
...
download_from_GCS_task = download_from_GCS_op(
    gcs_path=...,
)
```

## Other information

###### Tags

* input_type=[URI]

[URI]: https://github.com/Ark-kun/pipeline_components/tree/master/types/URI
<!-- END_GENERATED_CONTENT -->
