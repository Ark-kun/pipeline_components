<!-- BEGIN_GENERATED_CONTENT -->
# Convert column to categorical using Pandas on ApacheParquet data

Description: Changes column type to categorical.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/pandas/Convert_column_to_categorical/in_ApacheParquet_format/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Convert_column_to_categorical/in_ApacheParquet_format/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**table** **\***|[ApacheParquet]|||
|**column_name** **\***|[String]||Name of the column to convert|
|categories|[JsonArray]||A list of category names that should be used to map string values to indexes.<br/>If omitted, the mapping will be automatically generated from the column unique values.|

## Outputs

|Name|Type|Description|
|-|-|-|
|transformed_table|[ApacheParquet]||
|categories|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
convert_column_to_categorical_using_Pandas_on_ApacheParquet_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Convert_column_to_categorical/in_ApacheParquet_format/component.yaml")
...
convert_column_to_categorical_using_Pandas_on_ApacheParquet_data_task = convert_column_to_categorical_using_Pandas_on_ApacheParquet_data_op(
    table=...,
    column_name=...,
    # Optional:
    # categories=[...],
)
```

## Other information

###### Tags

* input_type=[ApacheParquet]
* input_type=[JsonArray]
* input_type=[String]
* output_type=[ApacheParquet]
* output_type=[JsonArray]

[ApacheParquet]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ApacheParquet
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
