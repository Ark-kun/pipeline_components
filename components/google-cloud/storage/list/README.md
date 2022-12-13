<!-- BEGIN_GENERATED_CONTENT -->
# List blobs

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/storage/list/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/storage/list/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**GCS path** **\***|[URI]||GCS path for listing. For recursive listing use the "gs://bucket/path/**" syntax".|

## Outputs

|Name|Type|Description|
|-|-|-|
|Paths|||

## Implementation

#### Container

Container image: [google/cloud-sdk](https://hub.docker.com/r/)

## Usage

```python
list_blobs_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/storage/list/component.yaml")
...
list_blobs_task = list_blobs_op(
    gcs_path=...,
)
```

## Other information

###### Tags

* input_type=[URI]

[URI]: https://github.com/Ark-kun/pipeline_components/tree/master/types/URI
<!-- END_GENERATED_CONTENT -->
