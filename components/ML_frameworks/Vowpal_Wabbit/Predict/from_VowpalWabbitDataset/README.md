<!-- BEGIN_GENERATED_CONTENT -->
# Predict using Vowpal Wabbit model on VowpalWabbitDataset

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/ML_frameworks/Vowpal_Wabbit/Predict/from_VowpalWabbitDataset/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Vowpal_Wabbit/Predict/from_VowpalWabbitDataset/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Dataset** **\***|[VowpalWabbitDataset]|||
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
predict_using_Vowpal_Wabbit_model_on_VowpalWabbitDataset_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Vowpal_Wabbit/Predict/from_VowpalWabbitDataset/component.yaml")
...
predict_using_Vowpal_Wabbit_model_on_VowpalWabbitDataset_task = predict_using_Vowpal_Wabbit_model_on_VowpalWabbitDataset_op(
    dataset=...,
    model=...,
)
```

## Other information

###### Tags

* input_type=[VowpalWabbitDataset]
* input_type=[VowpalWabbitRegressorModel]

[VowpalWabbitDataset]: https://github.com/Ark-kun/pipeline_components/tree/master/types/VowpalWabbitDataset
[VowpalWabbitRegressorModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/VowpalWabbitRegressorModel
<!-- END_GENERATED_CONTENT -->
