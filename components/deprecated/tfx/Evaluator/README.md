<!-- BEGIN_GENERATED_CONTENT -->
# Evaluator

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/Evaluator/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/Evaluator/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**examples** **\***|[Examples]|||
|model|[Model]|||
|baseline_model|[Model]|||
|schema|[Schema]|||
|eval_config|[JsonObject]: `{"data_type": "proto:tensorflow_model_analysis.EvalConfig"}`|||
|feature_slicing_spec|[JsonObject]: `{"data_type": "proto:tfx.components.evaluator.FeatureSlicingSpec"}`|||
|fairness_indicator_thresholds|[JsonArray]|||
|example_splits|[String]|||
|module_file|[String]|||
|module_path|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|evaluation|[ModelEvaluation]||
|blessing|[ModelBlessing]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
evaluator_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/Evaluator/component.yaml")
...
evaluator_task = evaluator_op(
    examples=...,
    # Optional:
    # model=...,
    # baseline_model=...,
    # schema=...,
    # eval_config=...,
    # feature_slicing_spec=...,
    # fairness_indicator_thresholds=[...],
    # example_splits=...,
    # module_file=...,
    # module_path=...,
)
```

## Other information

###### Tags

* input_type=[Examples]
* input_type=[JsonArray]
* input_type=[JsonObject]
* input_type=[Model]
* input_type=[Schema]
* input_type=[String]
* output_type=[ModelBlessing]
* output_type=[ModelEvaluation]

[Examples]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Examples
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[Model]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Model
[ModelBlessing]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ModelBlessing
[ModelEvaluation]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ModelEvaluation
[Schema]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Schema
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
