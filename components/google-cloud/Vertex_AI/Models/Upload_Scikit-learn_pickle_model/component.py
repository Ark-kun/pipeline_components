from typing import NamedTuple

from kfp.components import create_component_from_func, InputPath, OutputPath


def upload_Scikit_learn_pickle_model_to_Google_Cloud_Vertex_AI(
    model_path: InputPath("ScikitLearnPickleModel"),
    sklearn_version: str = None,

    display_name: str = None,
    description: str = None,

    # Uncomment when anyone requests these:
    # instance_schema_uri: str = None,
    # parameters_schema_uri: str = None,
    # prediction_schema_uri: str = None,
    # explanation_metadata: "google.cloud.aiplatform_v1.types.explanation_metadata.ExplanationMetadata" = None,
    # explanation_parameters: "google.cloud.aiplatform_v1.types.explanation.ExplanationParameters" = None,

    project: str = None,
    location: str = "us-central1",
    labels: dict = None,
    # encryption_spec_key_name: str = None,
    staging_bucket: str = None,
) -> NamedTuple("Outputs", [
    ("model_name", "GoogleCloudVertexAiModelName"),
    ("model_dict", dict),
]):
    import datetime
    import json
    import os
    import shutil
    import tempfile
    from google.cloud import aiplatform

    if not location:
        location = os.environ.get("CLOUD_ML_REGION")

    if not labels:
        labels = {}
    labels["component-source"] = "github-com-ark-kun-pipeline-components"

    # The serving container decides the model type based on the model file extension.
    # So we need to rename the mode file (e.g. /tmp/inputs/model/data) to *.pkl
    _, renamed_model_path = tempfile.mkstemp(suffix=".pkl")
    shutil.copyfile(src=model_path, dst=renamed_model_path)

    display_name = display_name or "Scikit-learn model " + datetime.datetime.now().isoformat(sep=" ")

    model = aiplatform.Model.upload_scikit_learn_model_file(
        model_file_path=renamed_model_path,
        sklearn_version=sklearn_version,

        display_name=display_name,
        description=description,

        # instance_schema_uri=instance_schema_uri,
        # parameters_schema_uri=parameters_schema_uri,
        # prediction_schema_uri=prediction_schema_uri,
        # explanation_metadata=explanation_metadata,
        # explanation_parameters=explanation_parameters,

        project=project,
        location=location,
        labels=labels,
        # encryption_spec_key_name=encryption_spec_key_name,
        staging_bucket=staging_bucket,
    )
    model_json = json.dumps(model.to_dict(), indent=2)
    print(model_json)
    return (model.resource_name, model_json)

if __name__ == "__main__":
    # Getting input descriptions
    # try:
    #     from google.cloud import aiplatform
    #     upload_Scikit_learn_model_to_Google_Cloud_Vertex_AI.__doc__ = aiplatform.Model.upload_scikit_learn_model_file.__doc__
    # except ImportError:
    #     pass

    upload_Scikit_learn_pickle_model_to_Google_Cloud_Vertex_AI_op = create_component_from_func(
        func=upload_Scikit_learn_pickle_model_to_Google_Cloud_Vertex_AI,
        base_image="python:3.9",
        packages_to_install=[
            # "google-cloud-aiplatform==1.10.0",
            "git+https://github.com/Ark-kun/python-aiplatform@9b50f62b9d1409644656fb3202edc7be19c722f4#egg=google-cloud-aiplatform&subdirectory=."   # branch: fix--Fixed-getitng-project-ID-when-running-on-Vertex-AI
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Upload_Scikit-learn_pickle_model/component.yaml",
        },
        output_component_file="component.yaml",
    )
