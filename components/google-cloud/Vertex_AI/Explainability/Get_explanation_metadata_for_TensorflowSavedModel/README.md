<!-- BEGIN_GENERATED_CONTENT -->
# Get explanation metadata for TensorflowSavedModel

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Vertex_AI/Explainability/Get_explanation_metadata_for_TensorflowSavedModel/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Explainability/Get_explanation_metadata_for_TensorflowSavedModel/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[TensorflowSavedModel]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|explanation_metadata|[JsonObject]||

## Implementation

#### Container

Container image: [tensorflow/tensorflow:2.9.1](https://hub.docker.com/r/tensorflow/tensorflow)

## Usage

```python
get_explanation_metadata_for_TensorflowSavedModel_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Explainability/Get_explanation_metadata_for_TensorflowSavedModel/component.yaml")
...
get_explanation_metadata_for_TensorflowSavedModel_task = get_explanation_metadata_for_TensorflowSavedModel_op(
    model=...,
)
```

## Other information

###### Tags

* input_type=[TensorflowSavedModel]
* output_type=[JsonObject]

[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[TensorflowSavedModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TensorflowSavedModel
<!-- END_GENERATED_CONTENT -->
