<!-- BEGIN_GENERATED_CONTENT -->
# Train regression model using Vowpal Wabbit on VowpalWabbitJsonDataset Train model using Keras on CSV

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/ML_frameworks/Vowpal_Wabbit/Train_regression_model/from_VowpalWabbitJsonDataset/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Vowpal_Wabbit/Train_regression_model/from_VowpalWabbitJsonDataset/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Dataset** **\***|[VowpalWabbitJsonDataset]|||
|Initial model|[VowpalWabbitRegressorModel]|||
|**Number of passes** **\***|[Integer]|1||
|**Loss function** **\***|[String]|squared|Supported values: squared, hinge, logistic, quantile, poisson. See https://github.com/VowpalWabbit/vowpal_wabbit/wiki/Loss-functions|

## Outputs

|Name|Type|Description|
|-|-|-|
|Model|[VowpalWabbitRegressorModel]||
|Readable model|[VowpalWabbitReadableHashRegressorModel]||

## Implementation

#### Container

Container image: [vowpalwabbit/vw-rel-alpine:9.0.1](https://hub.docker.com/r/vowpalwabbit/vw-rel-alpine)

## Usage

```python
train_regression_model_using_Vowpal_Wabbit_on_VowpalWabbitJsonDataset_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Vowpal_Wabbit/Train_regression_model/from_VowpalWabbitJsonDataset/component.yaml")
...
train_regression_model_using_Vowpal_Wabbit_on_VowpalWabbitJsonDataset_task = train_regression_model_using_Vowpal_Wabbit_on_VowpalWabbitJsonDataset_op(
    dataset=...,
    number_of_passes=...,
    loss_function=...,
    # Optional:
    # initial_model=...,
)
```

## Other information

###### Tags

* input_type=[Integer]
* input_type=[String]
* input_type=[VowpalWabbitJsonDataset]
* input_type=[VowpalWabbitRegressorModel]
* output_type=[VowpalWabbitReadableHashRegressorModel]
* output_type=[VowpalWabbitRegressorModel]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[VowpalWabbitJsonDataset]: https://github.com/Ark-kun/pipeline_components/tree/master/types/VowpalWabbitJsonDataset
[VowpalWabbitReadableHashRegressorModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/VowpalWabbitReadableHashRegressorModel
[VowpalWabbitRegressorModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/VowpalWabbitRegressorModel
<!-- END_GENERATED_CONTENT -->