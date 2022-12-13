<!-- BEGIN_GENERATED_CONTENT -->
# Train model using scikit learn from CSV

Description: Train any Scikit-learn model

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/ML_frameworks/Scikit_learn/Train_model/from_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Scikit_learn/Train_model/from_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dataset** **\***|[CSV]||Tabular dataset for training.|
|**label_column_name** **\***|[String]||Name of the table column to use as label.|
|**model_class_name** **\***|[String]||Full model class name. Example: `sklearn.linear_model.LogisticRegression`|
|model_parameters|[JsonObject]|{}|A dictionary of model class parameter values.|
|random_seed|[Integer]|0|Controls the seed of the random processes.|

## Outputs

|Name|Type|Description|
|-|-|-|
|model|[ScikitLearnPickleModel]|Trained model in Scikit-learn pickle format.|
|model_dict|[JsonObject]|Trained model in dictionary format.|

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
train_model_using_scikit_learn_from_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Scikit_learn/Train_model/from_CSV/component.yaml")
...
train_model_using_scikit_learn_from_CSV_task = train_model_using_scikit_learn_from_CSV_op(
    dataset=...,
    label_column_name=...,
    model_class_name=...,
    # Optional:
    # model_parameters="{}",
    # random_seed=0,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[Integer]
* input_type=[JsonObject]
* input_type=[String]
* output_type=[JsonObject]
* output_type=[ScikitLearnPickleModel]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[ScikitLearnPickleModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ScikitLearnPickleModel
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
