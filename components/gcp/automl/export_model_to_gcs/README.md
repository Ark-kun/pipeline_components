<!-- BEGIN_GENERATED_CONTENT -->
# Automl export model to gcs

Description: Exports a trained model to a user specified Google Cloud Storage location.

    Args:
        model_path: The resource name of the model to export. Format: 'projects/<project>/locations/<location>/models/<model>'
        gcs_output_uri_prefix: The Google Cloud Storage directory where the model should be written to. Must be in the same location as AutoML. Required location: us-central1.
        model_format: The format in which the model must be exported. The available, and default, formats depend on the problem and model type. Possible formats: tf_saved_model, tf_js, tflite, core_ml, edgetpu_tflite. See https://cloud.google.com/automl/docs/reference/rest/v1/projects.locations.models/export?hl=en#modelexportoutputconfig

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/gcp/automl/export_model_to_gcs/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/export_model_to_gcs/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model_path** **\***|[String]|||
|**gcs_output_uri_prefix** **\***|[String]|||
|model_format|[String]|tf_saved_model||

## Outputs

|Name|Type|Description|
|-|-|-|
|model_directory|[Uri]||

## Implementation

#### Container

Container image: [python:3.8](https://hub.docker.com/r/_/python)

## Usage

```python
automl_export_model_to_gcs_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/export_model_to_gcs/component.yaml")
...
automl_export_model_to_gcs_task = automl_export_model_to_gcs_op(
    model_path=...,
    gcs_output_uri_prefix=...,
    # Optional:
    # model_format="tf_saved_model",
)
```

## Other information

###### Tags

* input_type=[String]
* output_type=[Uri]

[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[Uri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Uri
<!-- END_GENERATED_CONTENT -->
