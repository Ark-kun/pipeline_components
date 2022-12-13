<!-- BEGIN_GENERATED_CONTENT -->
# Evaluator

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/deprecated/tfx/Evaluator/with_URI_IO/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/Evaluator/with_URI_IO/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**examples_uri** **\***|[ExamplesUri]|||
|**output_evaluation_uri** **\***|[ModelEvaluationUri]|||
|**output_blessing_uri** **\***|[ModelBlessingUri]|||
|model_uri|[ModelUri]|||
|baseline_model_uri|[ModelUri]|||
|schema_uri|[SchemaUri]|||
|eval_config|[JsonObject]: `{"data_type": "proto:tensorflow_model_analysis.EvalConfig"}`|||
|feature_slicing_spec|[JsonObject]: `{"data_type": "proto:tfx.components.evaluator.FeatureSlicingSpec"}`|||
|fairness_indicator_thresholds|[JsonArray]|||
|example_splits|[String]|||
|module_file|[String]|||
|module_path|[String]|||
|beam_pipeline_args|[JsonArray]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|evaluation_uri|[ModelEvaluationUri]||
|blessing_uri|[ModelBlessingUri]||

## Implementation

#### Container

Container image: [tensorflow/tfx:0.29.0](https://hub.docker.com/r/tensorflow/tfx)

## Usage

```python
evaluator_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/deprecated/tfx/Evaluator/with_URI_IO/component.yaml")
...
evaluator_task = evaluator_op(
    examples_uri=...,
    output_evaluation_uri=...,
    output_blessing_uri=...,
    # Optional:
    # model_uri=...,
    # baseline_model_uri=...,
    # schema_uri=...,
    # eval_config=...,
    # feature_slicing_spec=...,
    # fairness_indicator_thresholds=[...],
    # example_splits=...,
    # module_file=...,
    # module_path=...,
    # beam_pipeline_args=[...],
)
```

## Other information

###### Tags

* input_type=[ExamplesUri]
* input_type=[JsonArray]
* input_type=[JsonObject]
* input_type=[ModelBlessingUri]
* input_type=[ModelEvaluationUri]
* input_type=[ModelUri]
* input_type=[SchemaUri]
* input_type=[String]
* output_type=[ModelBlessingUri]
* output_type=[ModelEvaluationUri]

[ExamplesUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ExamplesUri
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[ModelBlessingUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ModelBlessingUri
[ModelEvaluationUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ModelEvaluationUri
[ModelUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ModelUri
[SchemaUri]: https://github.com/Ark-kun/pipeline_components/tree/master/types/SchemaUri
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
