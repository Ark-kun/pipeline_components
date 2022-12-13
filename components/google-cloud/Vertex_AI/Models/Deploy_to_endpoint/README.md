<!-- BEGIN_GENERATED_CONTENT -->
# Deploy model to endpoint for Google Cloud Vertex AI Model

Description: Deploys Google Cloud Vertex AI Model to a Google Cloud Vertex AI Endpoint.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Vertex_AI/Models/Deploy_to_endpoint/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Deploy_to_endpoint/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model_name** **\***|[GoogleCloudVertexAiModelName]||Full resource name of a Google Cloud Vertex AI Model|
|endpoint_name|[GoogleCloudVertexAiEndpointName]||Optional. Full name of Google Cloud Vertex Endpoint. A new<br/>endpoint is created if the name is not passed.|
|machine_type|[String]|n1-standard-2|The type of the machine. See the [list of machine types<br/>supported for prediction<br/>](https://cloud.google.com/vertex-ai/docs/predictions/configure-compute#machine-types).<br/>Defaults to "n1-standard-2"|
|min_replica_count|[Integer]|1|Optional. The minimum number of machine replicas this deployed<br/>model will be always deployed on. If traffic against it increases,<br/>it may dynamically be deployed onto more replicas, and as traffic<br/>decreases, some of these extra replicas may be freed.|
|max_replica_count|[Integer]|1|Optional. The maximum number of replicas this deployed model may<br/>be deployed on when the traffic against it increases. If requested<br/>value is too large, the deployment will error, but if deployment<br/>succeeds then the ability to scale the model to that many replicas<br/>is guaranteed (barring service outages). If traffic against the<br/>deployed model increases beyond what its replicas at maximum may<br/>handle, a portion of the traffic will be dropped. If this value<br/>is not provided, the smaller value of min_replica_count or 1 will<br/>be used.|
|accelerator_type|[String]||Optional. Hardware accelerator type. Must also set accelerator_count if used.<br/>One of ACCELERATOR_TYPE_UNSPECIFIED, NVIDIA_TESLA_K80, NVIDIA_TESLA_P100,<br/>NVIDIA_TESLA_V100, NVIDIA_TESLA_P4, NVIDIA_TESLA_T4|
|accelerator_count|[Integer]||Optional. The number of accelerators to attach to a worker replica.|

## Outputs

|Name|Type|Description|
|-|-|-|
|endpoint_name|[GoogleCloudVertexAiEndpointName]||
|endpoint_dict|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
deploy_model_to_endpoint_for_Google_Cloud_Vertex_AI_Model_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/Models/Deploy_to_endpoint/component.yaml")
...
deploy_model_to_endpoint_for_Google_Cloud_Vertex_AI_Model_task = deploy_model_to_endpoint_for_Google_Cloud_Vertex_AI_Model_op(
    model_name=...,
    # Optional:
    # endpoint_name=...,
    # machine_type="n1-standard-2",
    # min_replica_count=1,
    # max_replica_count=1,
    # accelerator_type=...,
    # accelerator_count=...,
)
```

## Other information

###### Tags

* input_type=[GoogleCloudVertexAiEndpointName]
* input_type=[GoogleCloudVertexAiModelName]
* input_type=[Integer]
* input_type=[String]
* output_type=[GoogleCloudVertexAiEndpointName]
* output_type=[JsonObject]

[GoogleCloudVertexAiEndpointName]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GoogleCloudVertexAiEndpointName
[GoogleCloudVertexAiModelName]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GoogleCloudVertexAiModelName
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
