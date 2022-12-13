<!-- BEGIN_GENERATED_CONTENT -->
# Automl import data from bigquery

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/gcp/automl/import_data_from_bigquery/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/import_data_from_bigquery/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dataset_path** **\***||||
|**input_uri** **\***|[String]|||
|retry||||
|timeout||||
|metadata|[JsonObject]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|dataset_path|[String]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
automl_import_data_from_bigquery_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/import_data_from_bigquery/component.yaml")
...
automl_import_data_from_bigquery_task = automl_import_data_from_bigquery_op(
    dataset_path=...,
    input_uri=...,
    # Optional:
    # retry=...,
    # timeout=...,
    # metadata={...},
)
```

## Other information

###### Tags

* input_type=[JsonObject]
* input_type=[String]
* output_type=[String]

[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
