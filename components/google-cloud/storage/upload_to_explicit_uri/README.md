<!-- BEGIN_GENERATED_CONTENT -->
# Upload to GCS Train model using Keras on CSV

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/storage/upload_to_explicit_uri/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/storage/upload_to_explicit_uri/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Data** **\***||||
|**GCS path** **\***|[URI]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|GCS path|[String]||

## Implementation

#### Container

Container image: [google/cloud-sdk](https://hub.docker.com/r/)

## Usage

```python
upload_to_GCS_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/storage/upload_to_explicit_uri/component.yaml")
...
upload_to_GCS_task = upload_to_GCS_op(
    data=...,
    gcs_path=...,
)
```

## Other information

###### Tags

* input_type=[URI]
* output_type=[String]

[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[URI]: https://github.com/Ark-kun/pipeline_components/tree/master/types/URI
<!-- END_GENERATED_CONTENT -->