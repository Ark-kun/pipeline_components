<!-- BEGIN_GENERATED_CONTENT -->
# Convert tsv to apache parquet

Description: Converts TSV table to Apache Parquet.

    [Apache Parquet](https://parquet.apache.org/)

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/ApacheParquet/from_TSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ApacheParquet/from_TSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data** **\***|[TSV]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|output_data|[ApacheParquet]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
convert_tsv_to_apache_parquet_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ApacheParquet/from_TSV/component.yaml")
...
convert_tsv_to_apache_parquet_task = convert_tsv_to_apache_parquet_op(
    data=...,
)
```

## Other information

###### Tags

* input_type=[TSV]
* output_type=[ApacheParquet]

[ApacheParquet]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ApacheParquet
[TSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TSV
<!-- END_GENERATED_CONTENT -->
