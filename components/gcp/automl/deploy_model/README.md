<!-- BEGIN_GENERATED_CONTENT -->
# Automl deploy model

Description: Deploys a trained model.

    Args:
        model_path: The resource name of the model to export. Format: 'projects/<project>/locations/<location>/models/<model>'

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/gcp/automl/deploy_model/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/deploy_model/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model_path** **\***|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|model_path|[String]||

## Implementation

#### Container

Container image: [python:3.8](https://hub.docker.com/r/_/python)

## Usage

```python
automl_deploy_model_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/deploy_model/component.yaml")
...
automl_deploy_model_task = automl_deploy_model_op(
    model_path=...,
)
```

## Other information

###### Tags

* input_type=[String]
* output_type=[String]

[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
