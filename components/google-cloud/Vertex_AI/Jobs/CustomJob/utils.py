import copy
import inspect
import json
import textwrap
from typing import Callable

from kfp import components
from kfp.components import structures


def convert_component_to_vertex_custom_job_payload(
    component_spec: structures.ComponentSpec,
    replica_count: int = None,
    machine_type: str = "e2-standard-4", # Required. https://cloud.google.com/vertex-ai/docs/training/configure-compute#machine-types
    accelerator_type: str = None, # https://cloud.google.com/vertex-ai/docs/reference/rest/v1/MachineSpec#acceleratortype
    accelerator_count: int = None,
) -> structures.ComponentSpec:
    component_container_spec = component_spec.implementation.container

    env_vars = []
    for name, value in (component_container_spec.env or {}).items():
        env_vars.append({
            "name": name,
            "value": value,
        })

    container_spec = {
        "imageUri": component_container_spec.image,
        #"command": !To be filled later!,
    }
    if env_vars:
        container_spec["env"] = env_vars

    machine_spec = {}
    if machine_type:
        assert isinstance(machine_type, str)
        machine_spec["machineType"] = machine_type
    if accelerator_type:
        assert isinstance(accelerator_type, str)
        machine_spec["acceleratorType"] = accelerator_type
    if accelerator_count:
        assert isinstance(accelerator_count, int)
        machine_spec["acceleratorCount"] = str(accelerator_count)

    worker_pool_spec = {
        "containerSpec": container_spec,
    }
    if machine_spec:
        worker_pool_spec["machineSpec"] = machine_spec

    if replica_count:
        assert isinstance(replica_count, int)
        assert replica_count > 0

    # "Both or none of `machine_spec` and `replica_count` should be specified."
    replica_count = replica_count or 1

    #worker_pool_spec["replicaCount"] = replica_count
    # "Replica count for master worker pool (worker_pool_specs[0].replica_count) should be 1."
    master_worker_pool_spec = worker_pool_spec.copy()
    master_worker_pool_spec["replica_count"] = 1
    
    worker_pool_specs = [master_worker_pool_spec]

    if replica_count > 1:
        worker_worker_pool_spec = worker_pool_spec.copy()
        worker_worker_pool_spec["replica_count"] = replica_count - 1
        worker_pool_specs.append(worker_worker_pool_spec)

    custom_job_spec = {
        "workerPoolSpecs": worker_pool_specs,
    }

    custom_job = {
        "displayName": component_spec.name or "Component",
        "jobSpec": custom_job_spec,
        "labels": {
            "alexey-volkov-customjob-launcher-util": "true",
        },
    }

    return custom_job

# Needs to be in sync with the `custom_job_launcher_main_code` function code
CUSTOM_JOB_REQUEST_CLI_PARAMETER = "--custom-job-request-template"

def custom_job_launcher_main_code():
    import json
    import sys
    from google.protobuf import json_format
    from google.cloud import aiplatform

    args = sys.argv[1:]
    
    assert args[0] == "--custom-job-request-template"
    custom_job_request = json.loads(args[1])
    # Command line arguments are located after ""--""
    command_line_args = args.copy()
    while command_line_args[0] != "--":
        command_line_args.pop(0)
    command_line_args.pop(0) # Skipping "--"

    custom_job_spec = custom_job_request["jobSpec"]
    worker_pool_specs = custom_job_spec["workerPoolSpecs"]
    for worker_pool_spec in worker_pool_specs:
        container_spec = worker_pool_spec["containerSpec"]
        container_spec["command"] = command_line_args

    # Converting the CustomJob structure to CustomJob proto
    custom_job_proto = aiplatform.jobs.gca_custom_job_compat.CustomJob()._pb # ! Note the `._pb`
    json_format.ParseDict(js_dict=custom_job_request, message=custom_job_proto)

    # Creating CustomJob object from CustomJob proto
    custom_job = aiplatform.CustomJob(
        display_name=None,
        worker_pool_specs=[],
        base_output_dir="gs://dummy",
        staging_bucket="gs://dummy",
    )
    custom_job._gca_resource = custom_job_proto
    custom_job.run()
    # TODO: Download and upload artifacts as needed when running on KFP.


def convert_component_to_run_using_custom_job(
    component_spec: structures.ComponentSpec,
    replica_count: int = None,
    machine_type: str = "e2-standard-4", # Required. https://cloud.google.com/vertex-ai/docs/training/configure-compute#machine-types
    accelerator_type: str = None, # https://cloud.google.com/vertex-ai/docs/reference/rest/v1/MachineSpec#acceleratortype
    accelerator_count: int = None,
) -> structures.ComponentSpec:
    custom_job_payload = convert_component_to_vertex_custom_job_payload(
        component_spec=component_spec,
        replica_count=replica_count,
        machine_type=machine_type,
        accelerator_type=accelerator_type,
        accelerator_count=accelerator_count,
    )
    
    custom_job_payload_json = json.dumps(custom_job_payload, indent=2)
    
    new_component_spec = copy.deepcopy(component_spec)
    
    container_spec = new_component_spec.implementation.container
    if not container_spec.command:
        raise ValueError("The component must have container command specified.")

    if container_spec.args:
        container_spec.command = container_spec.command + container_spec.args
    container_spec.args = None

    launcher_function_source = inspect.getsource(custom_job_launcher_main_code)
    # Getting the function body.
    # This assumes that the function signature is single-line
    launcher_function_body = textwrap.dedent("\n".join(launcher_function_source.split("\n")[1:]))
    
    launcher_command_line = [
        "sh",
        "-c",
        'PIP_DISABLE_PIP_VERSION_CHECK=1 python3 -m pip install --quiet --no-warn-script-location "google-cloud-aiplatform==1.17.1" --user && "$0" "$@"',
        "python3",
        "-u",
        "-c",
        launcher_function_body,
        CUSTOM_JOB_REQUEST_CLI_PARAMETER,
        custom_job_payload_json,
        "--",
    ]
    container_spec.command = launcher_command_line + container_spec.command
    container_spec.image = "python:3.10"
    
    return new_component_spec


def convert_op_to_run_using_custom_job(
    op: Callable,
    replica_count: int = None,
    machine_type: str = "e2-standard-4", # Required. https://cloud.google.com/vertex-ai/docs/training/configure-compute#machine-types
    accelerator_type: str = None, # https://cloud.google.com/vertex-ai/docs/reference/rest/v1/MachineSpec#acceleratortype
    accelerator_count: int = None,
) -> Callable:
    component_spec = op.component_spec

    new_component_spec = convert_component_to_run_using_custom_job(
        component_spec=component_spec,
        replica_count=replica_count,
        machine_type=machine_type,
        accelerator_type=accelerator_type,
        accelerator_count=accelerator_count,
    )

    new_op = components.load_component_from_text(json.dumps(new_component_spec.to_dict()))
    return new_op
