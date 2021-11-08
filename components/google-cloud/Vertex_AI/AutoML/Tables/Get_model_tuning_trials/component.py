from typing import NamedTuple

from kfp.components import create_component_from_func


def get_model_tuning_trials_for_Google_Cloud_Vertex_AI_AutoML_Tables(
    model_name: "GoogleCloudVertexAiModelName",
) -> NamedTuple("Outputs", [
    ("tuning_trials", list),  # List["type.googleapis.com/google.cloud.automl.master.TuningTrial"]
    ("model_structures", list),  # List["type.googleapis.com/google.cloud.automl.master.TablesModelStructure"]
    ("extra_entries", list),
]):
    import json
    from google.cloud import logging as cloud_logging

    (_, project, _, location, _, model_id) = model_name.split("/")

    # Need to specify project when initializing client.
    # Otherwise we'll get error when running on Vertex AI Pipelines:
    # google.api_core.exceptions.PermissionDenied: 403 The caller does not have permission
    cloud_logging_client = cloud_logging.Client(project=project)

    # Full filter:
    # resource.type="cloudml_job" resource.labels.job_id="{job_id}" resource.labels.project_id="{project_id}" labels.log_type="automl_tables" jsonPayload."@type"="type.googleapis.com/google.cloud.automl.master.TuningTrial"
    log_filter=f'resource.labels.job_id="{model_id}"'
    log_entry_list = list(cloud_logging_client.list_entries(filter_=log_filter))

    tuning_trials = []
    model_structures = []
    extra_entries = []
    for entry in log_entry_list:
        if entry.payload.get("@type") == "type.googleapis.com/google.cloud.automl.master.TuningTrial":
            tuning_trials.append(entry.payload)
        elif entry.payload.get("@type") == "type.googleapis.com/google.cloud.automl.master.TablesModelStructure":
            model_structures.append(entry.payload)
        else:
            extra_entries.append(entry.payload)
    
    # Manually serializing the results for pretty and stable output
    print("Tuning trials:")
    tuning_trials_json = json.dumps(tuning_trials, sort_keys=True, indent=2)
    print(tuning_trials_json)

    print("Model structures:")
    model_structures_json = json.dumps(model_structures, sort_keys=True, indent=2)
    print(model_structures_json)

    print("Extra entries:")
    extra_entries_json = json.dumps(extra_entries, sort_keys=True, indent=2)
    print(extra_entries_json)

    return (tuning_trials_json, model_structures_json, extra_entries_json)


if __name__ == '__main__':
    get_model_tuning_trials_for_Google_Cloud_Vertex_AI_AutoML_Tables_op = create_component_from_func(
        get_model_tuning_trials_for_Google_Cloud_Vertex_AI_AutoML_Tables,
        base_image="python:3.9",
        packages_to_install=["google-cloud-logging==2.7.0"],
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/AutoML/Tables/Get_model_tuning_trials/component.yaml",
        },
    )
