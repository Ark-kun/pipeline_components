<!-- BEGIN_GENERATED_CONTENT -->
# Automl create model for tables

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/gcp/automl/create_model_for_tables/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/create_model_for_tables/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**gcp_project_id** **\***|[String]|||
|**gcp_region** **\***|[String]|||
|**display_name** **\***|[String]|||
|**dataset_id** **\***|[String]|||
|target_column_path|[String]|||
|input_feature_column_paths|[JsonArray]|||
|optimization_objective|[String]|MAXIMIZE_AU_PRC||
|train_budget_milli_node_hours|[Integer]|1000||

## Outputs

|Name|Type|Description|
|-|-|-|
|model_path|[String]||
|model_id|[String]||
|model_page_url|[URI]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
automl_create_model_for_tables_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/create_model_for_tables/component.yaml")
...
automl_create_model_for_tables_task = automl_create_model_for_tables_op(
    gcp_project_id=...,
    gcp_region=...,
    display_name=...,
    dataset_id=...,
    # Optional:
    # target_column_path=...,
    # input_feature_column_paths=[...],
    # optimization_objective="MAXIMIZE_AU_PRC",
    # train_budget_milli_node_hours=1000,
)
```

## Other information

###### Tags

* input_type=[Integer]
* input_type=[JsonArray]
* input_type=[String]
* output_type=[String]
* output_type=[URI]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[URI]: https://github.com/Ark-kun/pipeline_components/tree/master/types/URI
<!-- END_GENERATED_CONTENT -->
