from typing import NamedTuple


def deploy_model_to_endpoint_for_Google_Cloud_Vertex_AI_Model(
    model_name: "GoogleCloudVertexAiModelName",
    endpoint_name: "GoogleCloudVertexAiEndpointName" = None,
    machine_type: str = "n1-standard-2",
    min_replica_count: int = 1,
    max_replica_count: int = 1,
    accelerator_type: str = None,
    accelerator_count: int = None,
    #
    # Uncomment when anyone requests these:
    # deployed_model_display_name: str = None,
    # traffic_percentage: int = 0,
    # traffic_split: dict = None,
    # service_account: str = None,
    # explanation_metadata: "google.cloud.aiplatform_v1.types.explanation_metadata.ExplanationMetadata" = None,
    # explanation_parameters: "google.cloud.aiplatform_v1.types.explanation.ExplanationParameters" = None,
    #
    # encryption_spec_key_name: str = None,
) -> NamedTuple(
    "Outputs",
    [
        ("endpoint_name", "GoogleCloudVertexAiEndpointName"),
        ("endpoint_dict", dict),
    ],
):
    """Deploys Google Cloud Vertex AI Model to a Google Cloud Vertex AI Endpoint.

    Args:
        model_name: Full resource name of a Google Cloud Vertex AI Model
        endpoint_name: Optional. Full name of Google Cloud Vertex Endpoint. A new
            endpoint is created if the name is not passed.
        machine_type: The type of the machine. See the [list of machine types
            supported for prediction
            ](https://cloud.google.com/vertex-ai/docs/predictions/configure-compute#machine-types).
            Defaults to "n1-standard-2"
        min_replica_count (int):
            Optional. The minimum number of machine replicas this deployed
            model will be always deployed on. If traffic against it increases,
            it may dynamically be deployed onto more replicas, and as traffic
            decreases, some of these extra replicas may be freed.
        max_replica_count (int):
            Optional. The maximum number of replicas this deployed model may
            be deployed on when the traffic against it increases. If requested
            value is too large, the deployment will error, but if deployment
            succeeds then the ability to scale the model to that many replicas
            is guaranteed (barring service outages). If traffic against the
            deployed model increases beyond what its replicas at maximum may
            handle, a portion of the traffic will be dropped. If this value
            is not provided, the smaller value of min_replica_count or 1 will
            be used.
        accelerator_type (str):
            Optional. Hardware accelerator type. Must also set accelerator_count if used.
            One of ACCELERATOR_TYPE_UNSPECIFIED, NVIDIA_TESLA_K80, NVIDIA_TESLA_P100,
            NVIDIA_TESLA_V100, NVIDIA_TESLA_P4, NVIDIA_TESLA_T4
        accelerator_count (int):
            Optional. The number of accelerators to attach to a worker replica.
    """
    import json
    from google.cloud import aiplatform

    model = aiplatform.Model(model_name=model_name)

    if endpoint_name:
        endpoint = aiplatform.Endpoint(endpoint_name=endpoint_name)
    else:
        endpoint_display_name = model.display_name[:118] + "_endpoint"
        endpoint = aiplatform.Endpoint.create(
            display_name=endpoint_display_name,
            project=model.project,
            location=model.location,
            # encryption_spec_key_name=encryption_spec_key_name,
            labels={"component-source": "github-com-ark-kun-pipeline-components"},
        )

    endpoint = model.deploy(
        endpoint=endpoint,
        # deployed_model_display_name=deployed_model_display_name,
        machine_type=machine_type,
        min_replica_count=min_replica_count,
        max_replica_count=max_replica_count,
        accelerator_type=accelerator_type,
        accelerator_count=accelerator_count,
        # service_account=service_account,
        # explanation_metadata=explanation_metadata,
        # explanation_parameters=explanation_parameters,
        # encryption_spec_key_name=encryption_spec_key_name,
    )

    endpoint_json = json.dumps(endpoint.to_dict(), indent=2)
    print(endpoint_json)
    return (endpoint.resource_name, endpoint_json)


if __name__ == "__main__":
    from kfp.components import create_component_from_func

    deploy_model_to_endpoint_for_Google_Cloud_Vertex_AI_Model_op = create_component_from_func(
        func=deploy_model_to_endpoint_for_Google_Cloud_Vertex_AI_Model,
        base_image="python:3.9",
        packages_to_install=[
            "google-cloud-aiplatform==1.7.0",
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Deploy_to_endpoint/component.yaml",
        },
        output_component_file="component.yaml",
    )
