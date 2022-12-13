<!-- BEGIN_GENERATED_CONTENT -->
# Fill all missing values using Pandas on ApacheParquet data

Description: Fills the missing column items with the specified replacement value.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/pandas/Fill_all_missing_values/in_ApacheParquet_format/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Fill_all_missing_values/in_ApacheParquet_format/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**table** **\***|[ApacheParquet]||Input data table.|
|replacement_value|[String]|0|The value to use when replacing the missing items.|
|column_names|[JsonArray]||Names of the columns where to perform the replacement.|

## Outputs

|Name|Type|Description|
|-|-|-|
|transformed_table|[ApacheParquet]|Transformed data table where missing values are filed.|

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
fill_all_missing_values_using_Pandas_on_ApacheParquet_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Fill_all_missing_values/in_ApacheParquet_format/component.yaml")
...
fill_all_missing_values_using_Pandas_on_ApacheParquet_data_task = fill_all_missing_values_using_Pandas_on_ApacheParquet_data_op(
    table=...,
    # Optional:
    # replacement_value="0",
    # column_names=[...],
)
```

## Other information

###### Tags

* input_type=[ApacheParquet]
* input_type=[JsonArray]
* input_type=[String]
* output_type=[ApacheParquet]

[ApacheParquet]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ApacheParquet
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
