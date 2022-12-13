<!-- BEGIN_GENERATED_CONTENT -->
# Convert apache arrow feather to apache parquet

Description: Converts Apache Arrow Feather to Apache Parquet.

    [Apache Arrow Feather](https://arrow.apache.org/docs/python/feather.html)
    [Apache Parquet](https://parquet.apache.org/)

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/_converters/ApacheParquet/from_ApacheArrowFeather/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ApacheParquet/from_ApacheArrowFeather/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data** **\***|[ApacheArrowFeather]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|output_data|[ApacheParquet]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
convert_apache_arrow_feather_to_apache_parquet_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ApacheParquet/from_ApacheArrowFeather/component.yaml")
...
convert_apache_arrow_feather_to_apache_parquet_task = convert_apache_arrow_feather_to_apache_parquet_op(
    data=...,
)
```

## Other information

###### Tags

* input_type=[ApacheArrowFeather]
* output_type=[ApacheParquet]

[ApacheArrowFeather]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ApacheArrowFeather
[ApacheParquet]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ApacheParquet
<!-- END_GENERATED_CONTENT -->
