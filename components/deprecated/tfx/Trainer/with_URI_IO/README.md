<!-- BEGIN_GENERATED_CONTENT -->
# Trainer

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/Trainer/with_URI_IO/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/Trainer/with_URI_IO/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**examples_uri** **\***|[ExamplesUri]|||
|**output_model_uri** **\***|[ModelUri]|||
|**output_model_run_uri** **\***|[ModelRunUri]|||
|**train_args** **\***|[JsonObject]: `{"data_type": "proto:tfx.components.trainer.TrainArgs"}`|||
|**eval_args** **\***|[JsonObject]: `{"data_type": "proto:tfx.components.trainer.EvalArgs"}`|||
|transform_graph_uri|[TransformGraphUri]|||
|schema_uri|[SchemaUri]|||
|base_model_uri|[ModelUri]|||
|hyperparameters_uri|[HyperParametersUri]|||
|module_file|[String]|||
|run_fn|[String]|||
|trainer_fn|[String]|||
|custom_config|[String]|||
|beam_pipeline_args|[JsonArray]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|model_uri|[ModelUri]||
|model_run_uri|[ModelRunUri]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
trainer_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/Trainer/with_URI_IO/component.yaml")
...
trainer_task = trainer_op(
    examples_uri=...,
    output_model_uri=...,
    output_model_run_uri=...,
    train_args=...,
    eval_args=...,
    # Optional:
    # transform_graph_uri=...,
    # schema_uri=...,
    # base_model_uri=...,
    # hyperparameters_uri=...,
    # module_file=...,
    # run_fn=...,
    # trainer_fn=...,
    # custom_config=...,
    # beam_pipeline_args=[...],
)
```

## Other information

###### Tags

* input_type=[ExamplesUri]
* input_type=[HyperParametersUri]
* input_type=[JsonArray]
* input_type=[JsonObject]
* input_type=[ModelRunUri]
* input_type=[ModelUri]
* input_type=[SchemaUri]
* input_type=[String]
* input_type=[TransformGraphUri]
* output_type=[ModelRunUri]
* output_type=[ModelUri]

[ExamplesUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ExamplesUri
[HyperParametersUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/HyperParametersUri
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[ModelRunUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ModelRunUri
[ModelUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ModelUri
[SchemaUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/SchemaUri
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[TransformGraphUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TransformGraphUri
<!-- END_GENERATED_CONTENT -->
