<!-- BEGIN_GENERATED_CONTENT -->
# Trainer

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/Trainer/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/Trainer/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**examples** **\***|[Examples]|||
|**train_args** **\***|[JsonObject]: `{"data_type": "proto:tfx.components.trainer.TrainArgs"}`|||
|**eval_args** **\***|[JsonObject]: `{"data_type": "proto:tfx.components.trainer.EvalArgs"}`|||
|transform_graph|[TransformGraph]|||
|schema|[Schema]|||
|base_model|[Model]|||
|hyperparameters|[HyperParameters]|||
|module_file|[String]|||
|run_fn|[String]|||
|trainer_fn|[String]|||
|custom_config|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|model|[Model]||
|model_run|[ModelRun]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
trainer_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/Trainer/component.yaml")
...
trainer_task = trainer_op(
    examples=...,
    train_args=...,
    eval_args=...,
    # Optional:
    # transform_graph=...,
    # schema=...,
    # base_model=...,
    # hyperparameters=...,
    # module_file=...,
    # run_fn=...,
    # trainer_fn=...,
    # custom_config=...,
)
```

## Other information

###### Tags

* input_type=[Examples]
* input_type=[HyperParameters]
* input_type=[JsonObject]
* input_type=[Model]
* input_type=[Schema]
* input_type=[String]
* input_type=[TransformGraph]
* output_type=[Model]
* output_type=[ModelRun]

[Examples]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Examples
[HyperParameters]: https://github.com/Ark-kun/pipeline_components/tree/master/types/HyperParameters
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[Model]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Model
[ModelRun]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ModelRun
[Schema]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Schema
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[TransformGraph]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TransformGraph
<!-- END_GENERATED_CONTENT -->
