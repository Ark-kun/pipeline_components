<!-- BEGIN_GENERATED_CONTENT -->
# Build SampledShapley explanation spec for Vertex AI

Description: Builds a SampledShapleyAttribution structure.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Vertex_AI/Explainability/Build_explanation_spec/SampledShapley/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Explainability/Build_explanation_spec/SampledShapley/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**explanation_metadata** **\***|[JsonObject]|||
|**path_count** **\***|[Integer]||The number of feature permutations to consider<br/>when approximating the Shapley values.<br/>Valid range of its value is [1, 50], inclusively.|
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
build_SampledShapley_explanation_spec_for_Vertex_AI_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Explainability/Build_explanation_spec/SampledShapley/component.yaml")
...
build_SampledShapley_explanation_spec_for_Vertex_AI_task = build_SampledShapley_explanation_spec_for_Vertex_AI_op(
    explanation_metadata=...,
    path_count=...,
    # Optional:
    # top_k=...,
    # output_indices=[...],
)
```

## Other information

###### Tags

* input_type=[Integer]
* input_type=[JsonArray]
* input_type=[JsonObject]
* output_type=[JsonObject]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
<!-- END_GENERATED_CONTENT -->
