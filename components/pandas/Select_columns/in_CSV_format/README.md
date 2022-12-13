<!-- BEGIN_GENERATED_CONTENT -->
# Select columns using Pandas on CSV data

Description: Selects columns from a data table.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/pandas/Select_columns/in_CSV_format/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Select_columns/in_CSV_format/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**table** **\***|[CSV]||Input data table.|
|**column_names** **\***|[JsonArray]||Names of the columns to select from the table.|

## Outputs

|Name|Type|Description|
|-|-|-|
|transformed_table|[CSV]|Transformed data table that only has the chosen columns.|

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
select_columns_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Select_columns/in_CSV_format/component.yaml")
...
select_columns_using_Pandas_on_CSV_data_task = select_columns_using_Pandas_on_CSV_data_op(
    table=...,
    column_names=...,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[JsonArray]
* output_type=[CSV]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
<!-- END_GENERATED_CONTENT -->
