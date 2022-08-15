from typing import NamedTuple
from kfp.components import create_component_from_func, InputPath, OutputPath


# https://cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#ExplanationParameters
def build_IntegratedGradients_explanation_spec_for_Vertex_AI(
    explanation_metadata: dict,  # google.cloud.aiplatform.explain.ExplanationMetadata
    # IntegratedGradientsAttribution
    step_count: int = 50,
    # smooth_grad_config: "google.cloud.aiplatform_v1beta1.types.SmoothGradConfig",
    noise_sigma: float = None,
    # blur_baseline_config: "google.cloud.aiplatform_v1beta1.types.BlurBaselineConfig",
    noisy_sample_count: int = None,
    max_blur_sigma: float = None,
    # feature_noise_sigma: "google.cloud.aiplatform_v1beta1.types.FeatureNoiseSigma",
    feature_noise_sigma: dict = None,
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
    """Builds a IntegratedGradientsAttribution structure.

    IntegratedGradients is an attribution method that computes Aumann-Shapley values taking advantage of the model's fully differentiable structure.
    Refer to this paper for more details: https://arxiv.org/abs/1703.01365

    Args:
        step_count: The number of steps for approximating the path
            integral. A good value to start is 50 and gradually increase
            until the sum to diff property is within the desired error
            range.
    """
    smooth_grad_config = {}
    if noisy_sample_count:
        smooth_grad_config["noisySampleCount"] = noisy_sample_count
    if noise_sigma:
        smooth_grad_config["noiseSigma"] = noise_sigma
    if feature_noise_sigma:
        smooth_grad_config["featureNoiseSigma"] = {
            "noiseSigma": [
                {"name": name, "sigma": sigma}
                for name, sigma in feature_noise_sigma.items()
            ]
        }

    integrated_gradients_attribution = {
        "stepCount": step_count,
    }
    if max_blur_sigma:
        integrated_gradients_attribution["blurBaselineConfig"] = {
            "maxBlurSigma": max_blur_sigma,
        }
    if smooth_grad_config:
        integrated_gradients_attribution["smoothGradConfig"] = smooth_grad_config

    explanation_parameters = {
        "integratedGradientsAttribution": integrated_gradients_attribution,
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
    build_IntegratedGradients_explanation_spec_for_Vertex_AI_op = create_component_from_func(
        build_IntegratedGradients_explanation_spec_for_Vertex_AI,
        output_component_file="component.yaml",
        base_image="python:3.10",
        packages_to_install=[],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Explainability/Build_explanation_spec/IntegratedGradients/component.yaml",
        },
    )
