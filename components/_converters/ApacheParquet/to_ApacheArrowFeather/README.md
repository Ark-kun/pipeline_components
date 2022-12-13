<!-- BEGIN_GENERATED_CONTENT -->
# Convert apache parquet to apache arrow feather

Description: Converts Apache Parquet to Apache Arrow Feather.

    [Apache Arrow Feather](https://arrow.apache.org/docs/python/feather.html)
    [Apache Parquet](https://parquet.apache.org/)

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/ApacheParquet/to_ApacheArrowFeather/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ApacheParquet/to_ApacheArrowFeather/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data** **\***|[ApacheParquet]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|output_data|[ApacheArrowFeather]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
convert_apache_parquet_to_apache_arrow_feather_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ApacheParquet/to_ApacheArrowFeather/component.yaml")
...
convert_apache_parquet_to_apache_arrow_feather_task = convert_apache_parquet_to_apache_arrow_feather_op(
    data=...,
)
```

## Other information

###### Tags

* input_type=[ApacheParquet]
* output_type=[ApacheArrowFeather]

[ApacheArrowFeather]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ApacheArrowFeather
[ApacheParquet]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ApacheParquet
<!-- END_GENERATED_CONTENT -->
