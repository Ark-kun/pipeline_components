<!-- BEGIN_GENERATED_CONTENT -->
# Convert apache parquet to csv

Description: Converts Apache Parquet to CSV.

    [Apache Parquet](https://parquet.apache.org/)

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/ApacheParquet/to_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ApacheParquet/to_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data** **\***|[ApacheParquet]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|output_data|[CSV]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
convert_apache_parquet_to_csv_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ApacheParquet/to_CSV/component.yaml")
...
convert_apache_parquet_to_csv_task = convert_apache_parquet_to_csv_op(
    data=...,
)
```

## Other information

###### Tags

* input_type=[ApacheParquet]
* output_type=[CSV]

[ApacheParquet]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ApacheParquet
[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
<!-- END_GENERATED_CONTENT -->
