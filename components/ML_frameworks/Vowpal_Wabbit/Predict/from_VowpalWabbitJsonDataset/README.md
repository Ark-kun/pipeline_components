<!-- BEGIN_GENERATED_CONTENT -->
# Predict using Vowpal Wabbit model on VowpalWabbitJsonDataset

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/ML_frameworks/Vowpal_Wabbit/Predict/from_VowpalWabbitJsonDataset/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Vowpal_Wabbit/Predict/from_VowpalWabbitJsonDataset/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Dataset** **\***|[VowpalWabbitJsonDataset]|||
|**Model** **\***|[VowpalWabbitRegressorModel]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Predictions|||

## Implementation

#### Container

Container image: [vowpalwabbit/vw-rel-alpine:9.0.1](https://hub.docker.com/r/vowpalwabbit/vw-rel-alpine)

## Usage

```python
predict_using_Vowpal_Wabbit_model_on_VowpalWabbitJsonDataset_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Vowpal_Wabbit/Predict/from_VowpalWabbitJsonDataset/component.yaml")
...
predict_using_Vowpal_Wabbit_model_on_VowpalWabbitJsonDataset_task = predict_using_Vowpal_Wabbit_model_on_VowpalWabbitJsonDataset_op(
    dataset=...,
    model=...,
)
```

## Other information

###### Tags

* input_type=[VowpalWabbitJsonDataset]
* input_type=[VowpalWabbitRegressorModel]

[VowpalWabbitJsonDataset]: https://github.com/Ark-kun/pipeline_components/tree/master/types/VowpalWabbitJsonDataset
[VowpalWabbitRegressorModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/VowpalWabbitRegressorModel
<!-- END_GENERATED_CONTENT -->
