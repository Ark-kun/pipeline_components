from typing import NamedTuple
from cloud_pipelines.components import create_component_from_func, InputPath, OutputPath


def get_explanation_metadata_for_TensorflowSavedModel(
    model_path: InputPath("TensorflowSavedModel"),
) -> NamedTuple("Outputs", [("explanation_metadata", dict),]):
    from google.cloud.aiplatform.explain.metadata.tf.v2 import (
        saved_model_metadata_builder,
    )

    explanation_metadata_builder = (
        saved_model_metadata_builder.SavedModelMetadataBuilder(model_path=model_path)
    )
    explanation_metadata = explanation_metadata_builder.get_metadata()
    return (explanation_metadata,)


if __name__ == "__main__":
    get_explanation_metadata_for_TensorflowSavedModel_op = create_component_from_func(
        get_explanation_metadata_for_TensorflowSavedModel,
        output_component_file="component.yaml",
        base_image="tensorflow/tensorflow:2.9.1",
        packages_to_install=["google-cloud-aiplatform==1.16.1"],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Explainability/Get_explanation_metadata_for_TensorflowSavedModel/component.yaml",
        },
    )
