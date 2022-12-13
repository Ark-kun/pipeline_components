<!-- BEGIN_GENERATED_CONTENT -->
# Binarize column using Pandas on CSV data

Description: Transforms a table column into a binary class column using a predicate.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/pandas/Binarize_column/in_CSV_format/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Binarize_column/in_CSV_format/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**table** **\***|[CSV]||Input data table.|
|**column_name** **\***|[String]||Name of the column to transform to binary class.|
|predicate|[String]|> 0|Expression that determines whether the column value is mapped to class 0 (false) or class 1 (true).|
|new_column_name|[String]||Name for the new class column. Equals column_name by default.|
|keep_original_column|[Boolean]|False|Whether to keep the original column (column_name) in the table.|

## Outputs

|Name|Type|Description|
|-|-|-|
|transformed_table|[CSV]|Transformed data table with the binary class column.|

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
binarize_column_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Binarize_column/in_CSV_format/component.yaml")
...
binarize_column_using_Pandas_on_CSV_data_task = binarize_column_using_Pandas_on_CSV_data_op(
    table=...,
    column_name=...,
    # Optional:
    # predicate="> 0",
    # new_column_name=...,
    # keep_original_column=False,
)
```

## Other information

###### Tags

* input_type=[Boolean]
* input_type=[CSV]
* input_type=[String]
* output_type=[CSV]

[Boolean]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Boolean
[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
