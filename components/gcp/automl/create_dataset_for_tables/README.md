<!-- BEGIN_GENERATED_CONTENT -->
# Create dataset for google cloud automl tables

Description: Creates an empty Dataset for AutoML tables

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/gcp/automl/create_dataset_for_tables/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/create_dataset_for_tables/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**display_name** **\***|[String]|||
|description|[String]|||
|tables_dataset_metadata|[JsonObject]|{}||
|gcp_project_id|[String]|||
|gcp_region|[String]|||
|retry_config|[JsonObject]|||
|timeout|[Float]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|dataset_name|[String]||
|dataset|[JsonObject]||
|dataset_path|[String]||
|create_time|[String]||
|dataset_id|[String]||
|dataset_url|[URI]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
create_dataset_for_google_cloud_automl_tables_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/create_dataset_for_tables/component.yaml")
...
create_dataset_for_google_cloud_automl_tables_task = create_dataset_for_google_cloud_automl_tables_op(
    display_name=...,
    # Optional:
    # description=...,
    # tables_dataset_metadata="{}",
    # gcp_project_id=...,
    # gcp_region=...,
    # retry_config={...},
    # timeout=...,
)
```

## Other information

###### Tags

* input_type=[Float]
* input_type=[JsonObject]
* input_type=[String]
* output_type=[JsonObject]
* output_type=[String]
* output_type=[URI]

[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[URI]: https://github.com/Ark-kun/pipeline_components/tree/master/types/URI
<!-- END_GENERATED_CONTENT -->
