<!-- BEGIN_GENERATED_CONTENT -->
# Convert apache parquet to tsv

Description: Converts Apache Parquet to TSV.

    [Apache Parquet](https://parquet.apache.org/)

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/ApacheParquet/to_TSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ApacheParquet/to_TSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data** **\***|[ApacheParquet]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|output_data|[TSV]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
convert_apache_parquet_to_tsv_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ApacheParquet/to_TSV/component.yaml")
...
convert_apache_parquet_to_tsv_task = convert_apache_parquet_to_tsv_op(
    data=...,
)
```

## Other information

###### Tags

* input_type=[ApacheParquet]
* output_type=[TSV]

[ApacheParquet]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ApacheParquet
[TSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TSV
<!-- END_GENERATED_CONTENT -->
