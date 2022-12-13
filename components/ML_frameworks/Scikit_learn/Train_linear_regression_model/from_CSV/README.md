<!-- BEGIN_GENERATED_CONTENT -->
# Train linear regression model using scikit learn from CSV

Description: Trains linear regression model using Scikit-learn.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/ML_frameworks/Scikit_learn/Train_linear_regression_model/from_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Scikit_learn/Train_linear_regression_model/from_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dataset** **\***|[CSV]||Tabular dataset for training.|
|**label_column_name** **\***|[String]||Name of the table column to use as label.|

## Outputs

|Name|Type|Description|
|-|-|-|
|model|[ScikitLearnPickleModel]|Trained model in Scikit-learn pickle format.|

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
train_linear_regression_model_using_scikit_learn_from_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Scikit_learn/Train_linear_regression_model/from_CSV/component.yaml")
...
train_linear_regression_model_using_scikit_learn_from_CSV_task = train_linear_regression_model_using_scikit_learn_from_CSV_op(
    dataset=...,
    label_column_name=...,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[String]
* output_type=[ScikitLearnPickleModel]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[ScikitLearnPickleModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ScikitLearnPickleModel
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
