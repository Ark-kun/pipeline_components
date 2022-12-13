<!-- BEGIN_GENERATED_CONTENT -->
# Create study in gcp ai platform optimizer

Description: Creates a Google Cloud AI Plaform Optimizer study.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Optimizer/Create_study/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Optimizer/Create_study/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**study_id** **\***|[String]||Name of the study.|
|**parameter_specs** **\***|[JsonArray]||List of parameter specs. See https://cloud.google.com/ai-platform/optimizer/docs/reference/rest/v1/projects.locations.studies#parameterspec|
|optimization_goal|[String]|MAXIMIZE|Optimization goal when optimizing a single metric. Can be MAXIMIZE (default) or MINIMIZE. Ignored if metric_specs list is provided.|
|metric_specs|[JsonArray]||List of metric specs. See https://cloud.google.com/ai-platform/optimizer/docs/reference/rest/v1/projects.locations.studies#metricspec|
|gcp_project_id|[String]|||
|gcp_region|[String]|us-central1||

## Outputs

|Name|Type|Description|
|-|-|-|
|study_name|[String]||

## Implementation

#### Container

Container image: [python:3.8](https://hub.docker.com/r/_/python)

## Usage

```python
create_study_in_gcp_ai_platform_optimizer_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Optimizer/Create_study/component.yaml")
...
create_study_in_gcp_ai_platform_optimizer_task = create_study_in_gcp_ai_platform_optimizer_op(
    study_id=...,
    parameter_specs=...,
    # Optional:
    # optimization_goal="MAXIMIZE",
    # metric_specs=[...],
    # gcp_project_id=...,
    # gcp_region="us-central1",
)
```

## Other information

###### Tags

* input_type=[JsonArray]
* input_type=[String]
* output_type=[String]

[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
