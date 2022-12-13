<!-- BEGIN_GENERATED_CONTENT -->
# Pandas Transform DataFrame in CSV format

Description: Transform DataFrame loaded from a CSV file.

    Inputs:
        table: Table to transform.
        transform_code: Transformation code. Code is written in Python and can consist of multiple lines.
            The DataFrame variable is called "df".
            Examples:
            - `df['prod'] = df['X'] * df['Y']`
            - `df = df[['X', 'prod']]`
            - `df.insert(0, "is_positive", df["X"] > 0)`

    Outputs:
        transformed_table: Transformed table.

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**table** **\***|[CSV]|||
|**transform_code** **\***|[PythonCode]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|transformed_table|[CSV]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
pandas_Transform_DataFrame_in_CSV_format_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml")
...
pandas_Transform_DataFrame_in_CSV_format_task = pandas_Transform_DataFrame_in_CSV_format_op(
    table=...,
    transform_code=...,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[PythonCode]
* output_type=[CSV]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[PythonCode]: https://github.com/Ark-kun/pipeline_components/tree/master/types/PythonCode
<!-- END_GENERATED_CONTENT -->
