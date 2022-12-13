<!-- BEGIN_GENERATED_CONTENT -->
# Transform using Pandas DataFrame on JsonLines data

Description: Transform DataFrame loaded from an ApacheParquet file.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/pandas/Transform_DataFrame/in_JsonLines_format/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Transform_DataFrame/in_JsonLines_format/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**table** **\***|[JsonLines]||DataFrame to transform.|
|**transform_code** **\***|[PythonCode]||Transformation code. Code is written in Python and can consist of multiple lines.<br/>The DataFrame variable is called "df".<br/>Examples:<br/>- `df['prod'] = df['X'] * df['Y']`<br/>- `df = df[['X', 'prod']]`<br/>- `df.insert(0, "is_positive", df["X"] > 0)`|

## Outputs

|Name|Type|Description|
|-|-|-|
|transformed_table|[JsonLines]|Transformed DataFrame.|

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
transform_using_Pandas_DataFrame_on_JsonLines_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Transform_DataFrame/in_JsonLines_format/component.yaml")
...
transform_using_Pandas_DataFrame_on_JsonLines_data_task = transform_using_Pandas_DataFrame_on_JsonLines_data_op(
    table=...,
    transform_code=...,
)
```

## Other information

###### Tags

* input_type=[JsonLines]
* input_type=[PythonCode]
* output_type=[JsonLines]

[JsonLines]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonLines
[PythonCode]: https://github.com/Ark-kun/pipeline_components/tree/master/types/PythonCode
<!-- END_GENERATED_CONTENT -->
