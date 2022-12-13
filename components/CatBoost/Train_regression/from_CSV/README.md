<!-- BEGIN_GENERATED_CONTENT -->
# Catboost train regression

Description: Train a CatBoost classifier model.

    Args:
        training_data_path: Path for the training data in CSV format.
        model_path: Output path for the trained model in binary CatBoostModel format.
        starting_model_path: Path for the existing trained model to start from.
        label_column: Column containing the label data.

        loss_function: The metric to use in training and also selector of the machine learning
            problem to solve. Default = 'RMSE'. Possible values:
            'RMSE', 'MAE', 'Quantile:alpha=value', 'LogLinQuantile:alpha=value', 'Poisson', 'MAPE', 'Lq:q=value'
        num_iterations: Number of trees to add to the ensemble.
        learning_rate: Step size shrinkage used in update to prevents overfitting.
            Default value is selected automatically for binary classification with other parameters set to default.
            In all other cases default is 0.03.
        depth: Depth of a tree. All trees are the same depth. Default = 6
        random_seed: Random number seed. Default = 0

        cat_features: A list of Categorical features (indices or names).
        additional_training_options: A dictionary with additional options to pass to CatBoostRegressor

    Outputs:
        model: Trained model in binary CatBoostModel format.

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/CatBoost/Train_regression/from_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/CatBoost/Train_regression/from_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**training_data** **\***|[CSV]|||
|starting_model|[CatBoostModel]|||
|label_column|[Integer]|0||
|loss_function|[String]|RMSE||
|num_iterations|[Integer]|500||
|learning_rate|[Float]|||
|depth|[Integer]|6||
|random_seed|[Integer]|0||
|cat_features|[JsonArray]|||
|additional_training_options|[JsonObject]|{}||

## Outputs

|Name|Type|Description|
|-|-|-|
|model|[CatBoostModel]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
catboost_train_regression_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/CatBoost/Train_regression/from_CSV/component.yaml")
...
catboost_train_regression_task = catboost_train_regression_op(
    training_data=...,
    # Optional:
    # starting_model=...,
    # label_column=0,
    # loss_function="RMSE",
    # num_iterations=500,
    # learning_rate=...,
    # depth=6,
    # random_seed=0,
    # cat_features=[...],
    # additional_training_options="{}",
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[CatBoostModel]
* input_type=[Float]
* input_type=[Integer]
* input_type=[JsonArray]
* input_type=[JsonObject]
* input_type=[String]
* output_type=[CatBoostModel]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[CatBoostModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CatBoostModel
[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
