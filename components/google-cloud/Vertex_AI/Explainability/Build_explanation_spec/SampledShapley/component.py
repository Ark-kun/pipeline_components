from typing import NamedTuple
from cloud_pipelines.components import create_component_from_func, InputPath, OutputPath


# https://cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#ExplanationParameters
def build_SampledShapley_explanation_spec_for_Vertex_AI(
    explanation_metadata: dict,  # google.cloud.aiplatform.explain.ExplanationMetadata
    # SampledShapleyAttribution
    path_count: int,
    # Common parameters
    top_k: int = None,
    output_indices: list = None,
) -> NamedTuple(
    "Outputs",
    [
        # ("explanation_parameters", "GoogleCloudVertexAIExplanationParameters"),
        ("explanation_parameters", dict),
    ],
):
    """Builds a SampledShapleyAttribution structure.

    SampledShapley is an attribution method that approximates Shapley values for features that contribute to the label being predicted.
    A sampling strategy is used to approximate the value rather than considering all subsets of features.
    Refer to this paper for model details: https://arxiv.org/abs/1306.4265.

    Args:
        path_count: The number of feature permutations to consider
            when approximating the Shapley values.
            Valid range of its value is [1, 50], inclusively.
    """
    explanation_parameters = {
        "sampledShapleyAttribution": {
            "pathCount": path_count,
        },
    }
    if top_k:
        explanation_parameters["topK"] = top_k
    if output_indices:
        explanation_parameters["outputIndices"] = output_indices

    explanation_spec = {
        "parameters": explanation_parameters,
        "metadata": explanation_metadata,
    }
    return (explanation_spec,)


if __name__ == "__main__":
    build_SampledShapley_explanation_spec_for_Vertex_AI_op = create_component_from_func(
        build_SampledShapley_explanation_spec_for_Vertex_AI,
        output_component_file="component.yaml",
        base_image="python:3.10",
        packages_to_install=[],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Explainability/Build_explanation_spec/SampledShapley/component.yaml",
        },
    )
