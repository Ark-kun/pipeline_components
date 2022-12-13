<!-- BEGIN_GENERATED_CONTENT -->
# Build IntegratedGradients explanation spec for Vertex AI

Description: Builds a IntegratedGradientsAttribution structure.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Vertex_AI/Explainability/Build_explanation_spec/IntegratedGradients/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Explainability/Build_explanation_spec/IntegratedGradients/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**explanation_metadata** **\***|[JsonObject]|||
|step_count|[Integer]|50|The number of steps for approximating the path<br/>integral. A good value to start is 50 and gradually increase<br/>until the sum to diff property is within the desired error<br/>range.|
|noise_sigma|[Float]|||
|noisy_sample_count|[Integer]|||
|max_blur_sigma|[Float]|||
|feature_noise_sigma|[JsonObject]|||
|top_k|[Integer]|||
|output_indices|[JsonArray]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|explanation_parameters|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
build_IntegratedGradients_explanation_spec_for_Vertex_AI_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Explainability/Build_explanation_spec/IntegratedGradients/component.yaml")
...
build_IntegratedGradients_explanation_spec_for_Vertex_AI_task = build_IntegratedGradients_explanation_spec_for_Vertex_AI_op(
    explanation_metadata=...,
    # Optional:
    # step_count=50,
    # noise_sigma=...,
    # noisy_sample_count=...,
    # max_blur_sigma=...,
    # feature_noise_sigma={...},
    # top_k=...,
    # output_indices=[...],
)
```

## Other information

###### Tags

* input_type=[Float]
* input_type=[Integer]
* input_type=[JsonArray]
* input_type=[JsonObject]
* output_type=[JsonObject]

[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
<!-- END_GENERATED_CONTENT -->
