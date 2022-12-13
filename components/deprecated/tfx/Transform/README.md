<!-- BEGIN_GENERATED_CONTENT -->
# Transform

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/Transform/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/Transform/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**examples** **\***|[Examples]|||
|**schema** **\***|[Schema]|||
|analyzer_cache|[TransformCache]|||
|module_file|[String]|||
|preprocessing_fn|[String]|||
|force_tf_compat_v1|[Integer]|||
|custom_config|[String]|||
|splits_config|[JsonObject]: `{"data_type": "proto:tfx.components.transform.SplitsConfig"}`|||

## Outputs

|Name|Type|Description|
|-|-|-|
|transform_graph|[TransformGraph]||
|transformed_examples|[Examples]||
|updated_analyzer_cache|[TransformCache]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
transform_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/Transform/component.yaml")
...
transform_task = transform_op(
    examples=...,
    schema=...,
    # Optional:
    # analyzer_cache=...,
    # module_file=...,
    # preprocessing_fn=...,
    # force_tf_compat_v1=...,
    # custom_config=...,
    # splits_config=...,
)
```

## Other information

###### Tags

* input_type=[Examples]
* input_type=[Integer]
* input_type=[JsonObject]
* input_type=[Schema]
* input_type=[String]
* input_type=[TransformCache]
* output_type=[Examples]
* output_type=[TransformCache]
* output_type=[TransformGraph]

[Examples]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Examples
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[Schema]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Schema
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[TransformCache]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TransformCache
[TransformGraph]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TransformGraph
<!-- END_GENERATED_CONTENT -->
