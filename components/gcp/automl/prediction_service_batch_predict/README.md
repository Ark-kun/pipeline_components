<!-- BEGIN_GENERATED_CONTENT -->
# Automl prediction service batch predict

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/gcp/automl/prediction_service_batch_predict/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/prediction_service_batch_predict/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model_path** **\***||||
|gcs_input_uris|[JsonArray]|||
|gcs_output_uri_prefix|[String]|||
|bq_input_uri|[String]|||
|bq_output_uri|[String]|||
|params||||
|retry||||
|timeout||||
|metadata|[JsonObject]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|gcs_output_directory|[String]||
|bigquery_output_dataset|[String]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
automl_prediction_service_batch_predict_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/prediction_service_batch_predict/component.yaml")
...
automl_prediction_service_batch_predict_task = automl_prediction_service_batch_predict_op(
    model_path=...,
    # Optional:
    # gcs_input_uris=[...],
    # gcs_output_uri_prefix=...,
    # bq_input_uri=...,
    # bq_output_uri=...,
    # params=...,
    # retry=...,
    # timeout=...,
    # metadata={...},
)
```

## Other information

###### Tags

* input_type=[JsonArray]
* input_type=[JsonObject]
* input_type=[String]
* output_type=[String]

[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
