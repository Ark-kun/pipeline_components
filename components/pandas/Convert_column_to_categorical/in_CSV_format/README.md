<!-- BEGIN_GENERATED_CONTENT -->
# Convert column to categorical using Pandas on CSV data

Description: Replaces string values with category indexes.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/pandas/Convert_column_to_categorical/in_CSV_format/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Convert_column_to_categorical/in_CSV_format/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**table** **\***|[CSV]|||
|**column_name** **\***|[String]||Name of the column to convert|
|categories|[JsonArray]||A list of category names that should be used to map string values to indexes.<br/>If omitted, the mapping will be automatically generated from the column unique values.|

## Outputs

|Name|Type|Description|
|-|-|-|
|transformed_table|[CSV]||
|categories|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
convert_column_to_categorical_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Convert_column_to_categorical/in_CSV_format/component.yaml")
...
convert_column_to_categorical_using_Pandas_on_CSV_data_task = convert_column_to_categorical_using_Pandas_on_CSV_data_op(
    table=...,
    column_name=...,
    # Optional:
    # categories=[...],
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[JsonArray]
* input_type=[String]
* output_type=[CSV]
* output_type=[JsonArray]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
