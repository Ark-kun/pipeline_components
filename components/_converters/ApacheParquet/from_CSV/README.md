<!-- BEGIN_GENERATED_CONTENT -->
# Convert csv to apache parquet

Description: Converts CSV table to Apache Parquet.

    [Apache Parquet](https://parquet.apache.org/)

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/ApacheParquet/from_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ApacheParquet/from_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data** **\***|[CSV]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|output_data|[ApacheParquet]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
convert_csv_to_apache_parquet_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ApacheParquet/from_CSV/component.yaml")
...
convert_csv_to_apache_parquet_task = convert_csv_to_apache_parquet_op(
    data=...,
)
```

## Other information

###### Tags

* input_type=[CSV]
* output_type=[ApacheParquet]

[ApacheParquet]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ApacheParquet
[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
<!-- END_GENERATED_CONTENT -->
