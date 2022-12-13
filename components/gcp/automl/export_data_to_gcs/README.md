<!-- BEGIN_GENERATED_CONTENT -->
# Automl export data to gcs

Description: Exports dataset data to GCS.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/gcp/automl/export_data_to_gcs/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/export_data_to_gcs/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dataset_path** **\***|[String]|||
|gcs_output_uri_prefix|[String]|||
|timeout|[Float]|||
|metadata|[JsonObject]|{}||

## Outputs

|Name|Type|Description|
|-|-|-|
|gcs_output_uri_prefix|[String]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
automl_export_data_to_gcs_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/export_data_to_gcs/component.yaml")
...
automl_export_data_to_gcs_task = automl_export_data_to_gcs_op(
    dataset_path=...,
    # Optional:
    # gcs_output_uri_prefix=...,
    # timeout=...,
    # metadata="{}",
)
```

## Other information

###### Tags

* input_type=[Float]
* input_type=[JsonObject]
* input_type=[String]
* output_type=[String]

[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
