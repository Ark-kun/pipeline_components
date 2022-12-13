<!-- BEGIN_GENERATED_CONTENT -->
# Select columns using Pandas on ApacheParquet data

Description: Selects columns from a data table.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/pandas/Select_columns/in_ApacheParquet_format/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Select_columns/in_ApacheParquet_format/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**table** **\***|[ApacheParquet]||Input data table.|
|**column_names** **\***|[JsonArray]||Names of the columns to select from the table.|

## Outputs

|Name|Type|Description|
|-|-|-|
|transformed_table|[ApacheParquet]|Transformed data table that only has the chosen columns.|

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
select_columns_using_Pandas_on_ApacheParquet_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Select_columns/in_ApacheParquet_format/component.yaml")
...
select_columns_using_Pandas_on_ApacheParquet_data_task = select_columns_using_Pandas_on_ApacheParquet_data_op(
    table=...,
    column_names=...,
)
```

## Other information

###### Tags

* input_type=[ApacheParquet]
* input_type=[JsonArray]
* output_type=[ApacheParquet]

[ApacheParquet]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ApacheParquet
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
<!-- END_GENERATED_CONTENT -->
