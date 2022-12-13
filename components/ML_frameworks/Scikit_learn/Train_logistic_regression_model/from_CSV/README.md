<!-- BEGIN_GENERATED_CONTENT -->
# Train logistic regression model using scikit learn from CSV

Description: Trains logistic regression model using Scikit-learn.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/ML_frameworks/Scikit_learn/Train_logistic_regression_model/from_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Scikit_learn/Train_logistic_regression_model/from_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dataset** **\***|[CSV]||Tabular dataset for training.|
|**label_column_name** **\***|[String]||Name of the data column to use as label.|
|penalty|[String]|l2|Used to specify the norm used in the penalization.<br/>Possible values: {'l1', 'l2', 'elasticnet', 'none'}, default='l2'<br/>The 'newton-cg',<br/>'sag' and 'lbfgs' solvers support only l2 penalties. 'elasticnet' is<br/>only supported by the 'saga' solver. If 'none' (not supported by the<br/>liblinear solver), no regularization is applied.|
|solver|[String]|lbfgs|Algorithm to use in the optimization problem.<br/>Possible values: {'newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'}, default='lbfgs'<br/><br/>- For small datasets, 'liblinear' is a good choice, whereas 'sag' and<br/>'saga' are faster for large ones.<br/>- For multiclass problems, only 'newton-cg', 'sag', 'saga' and 'lbfgs'<br/>handle multinomial loss; 'liblinear' is limited to one-versus-rest<br/>schemes.<br/>- 'newton-cg', 'lbfgs', 'sag' and 'saga' handle L2 or no penalty<br/>- 'liblinear' and 'saga' also handle L1 penalty<br/>- 'saga' also supports 'elasticnet' penalty<br/>- 'liblinear' does not support setting ``penalty='none'``<br/><br/>Note that 'sag' and 'saga' fast convergence is only guaranteed on<br/>features with approximately the same scale. You can<br/>preprocess the data with a scaler from sklearn.preprocessing.|
|max_iterations|[Integer]|100|Maximum number of iterations taken for the solvers to converge.|
|multi_class_mode|[String]|auto|Possible values: {'auto', 'ovr', 'multinomial'}, default='auto'<br/>If the option chosen is 'ovr', then a binary problem is fit for each<br/>label. For 'multinomial' the loss minimised is the multinomial loss fit<br/>across the entire probability distribution, *even when the data is<br/>binary*. 'multinomial' is unavailable when solver='liblinear'.<br/>'auto' selects 'ovr' if the data is binary, or if solver='liblinear',<br/>and otherwise selects 'multinomial'.|
|random_seed|[Integer]|0|Controls the seed of the random processes.|

## Outputs

|Name|Type|Description|
|-|-|-|
|model|[ScikitLearnPickleModel]|Trained model in Scikit-learn pickle format.|
|model_parameters|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
train_logistic_regression_model_using_scikit_learn_from_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Scikit_learn/Train_logistic_regression_model/from_CSV/component.yaml")
...
train_logistic_regression_model_using_scikit_learn_from_CSV_task = train_logistic_regression_model_using_scikit_learn_from_CSV_op(
    dataset=...,
    label_column_name=...,
    # Optional:
    # penalty="l2",
    # solver="lbfgs",
    # max_iterations=100,
    # multi_class_mode="auto",
    # random_seed=0,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[Integer]
* input_type=[String]
* output_type=[JsonObject]
* output_type=[ScikitLearnPickleModel]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[ScikitLearnPickleModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ScikitLearnPickleModel
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
