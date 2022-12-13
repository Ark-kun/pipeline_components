<!-- BEGIN_GENERATED_CONTENT -->
# Automl split dataset table column names

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/gcp/automl/split_dataset_table_column_names/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/split_dataset_table_column_names/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dataset_path** **\***|[String]|||
|**target_column_name** **\***|[String]|||
|table_index|[Integer]|0||

## Outputs

|Name|Type|Description|
|-|-|-|
|target_column_path|[String]||
|feature_column_paths|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
automl_split_dataset_table_column_names_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/gcp/automl/split_dataset_table_column_names/component.yaml")
...
automl_split_dataset_table_column_names_task = automl_split_dataset_table_column_names_op(
    dataset_path=...,
    target_column_name=...,
    # Optional:
    # table_index=0,
)
```

## Other information

###### Tags

* input_type=[Integer]
* input_type=[String]
* output_type=[JsonArray]
* output_type=[String]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
