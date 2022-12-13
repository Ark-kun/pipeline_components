<!-- BEGIN_GENERATED_CONTENT -->
# Transform

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/Transform/with_URI_IO/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/Transform/with_URI_IO/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**examples_uri** **\***|[ExamplesUri]|||
|**schema_uri** **\***|[SchemaUri]|||
|**output_transform_graph_uri** **\***|[TransformGraphUri]|||
|**output_transformed_examples_uri** **\***|[ExamplesUri]|||
|**output_updated_analyzer_cache_uri** **\***|[TransformCacheUri]|||
|analyzer_cache_uri|[TransformCacheUri]|||
|module_file|[String]|||
|preprocessing_fn|[String]|||
|force_tf_compat_v1|[Integer]|||
|custom_config|[String]|||
|splits_config|[JsonObject]: `{"data_type": "proto:tfx.components.transform.SplitsConfig"}`|||
|beam_pipeline_args|[JsonArray]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|transform_graph_uri|[TransformGraphUri]||
|transformed_examples_uri|[ExamplesUri]||
|updated_analyzer_cache_uri|[TransformCacheUri]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
transform_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/Transform/with_URI_IO/component.yaml")
...
transform_task = transform_op(
    examples_uri=...,
    schema_uri=...,
    output_transform_graph_uri=...,
    output_transformed_examples_uri=...,
    output_updated_analyzer_cache_uri=...,
    # Optional:
    # analyzer_cache_uri=...,
    # module_file=...,
    # preprocessing_fn=...,
    # force_tf_compat_v1=...,
    # custom_config=...,
    # splits_config=...,
    # beam_pipeline_args=[...],
)
```

## Other information

###### Tags

* input_type=[ExamplesUri]
* input_type=[Integer]
* input_type=[JsonArray]
* input_type=[JsonObject]
* input_type=[SchemaUri]
* input_type=[String]
* input_type=[TransformCacheUri]
* input_type=[TransformGraphUri]
* output_type=[ExamplesUri]
* output_type=[TransformCacheUri]
* output_type=[TransformGraphUri]

[ExamplesUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ExamplesUri
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[SchemaUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/SchemaUri
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[TransformCacheUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TransformCacheUri
[TransformGraphUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TransformGraphUri
<!-- END_GENERATED_CONTENT -->
