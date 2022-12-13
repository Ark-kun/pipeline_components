<!-- BEGIN_GENERATED_CONTENT -->
# Train XGBoost model on CSV

Description: Trains an XGBoost model.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/XGBoost/Train/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/XGBoost/Train/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**training_data** **\***|[CSV]||Training data in CSV format.|
|**label_column_name** **\***|[String]||Name of the column containing the label data.|
|starting_model|[XGBoostModel]||Existing trained model to start from (in the binary XGBoost format).|
|num_iterations|[Integer]|10|Number of boosting iterations.|
|objective|[String]|reg:squarederror|The learning task and the corresponding learning objective.<br/>See https://xgboost.readthedocs.io/en/latest/parameter.html#learning-task-parameters<br/>The most common values are:<br/>"reg:squarederror" - Regression with squared loss (default).<br/>"reg:logistic" - Logistic regression.<br/>"binary:logistic" - Logistic regression for binary classification, output probability.<br/>"binary:logitraw" - Logistic regression for binary classification, output score before logistic transformation<br/>"rank:pairwise" - Use LambdaMART to perform pairwise ranking where the pairwise loss is minimized<br/>"rank:ndcg" - Use LambdaMART to perform list-wise ranking where Normalized Discounted Cumulative Gain (NDCG) is maximized|
|booster|[String]|gbtree|The booster to use. Can be `gbtree`, `gblinear` or `dart`; `gbtree` and `dart` use tree based models while `gblinear` uses linear functions.|
|learning_rate|[Float]|0.3|Step size shrinkage used in update to prevents overfitting. Range: [0,1].|
|min_split_loss|[Float]|0|Minimum loss reduction required to make a further partition on a leaf node of the tree.<br/>The larger `min_split_loss` is, the more conservative the algorithm will be. Range: [0,Inf].|
|max_depth|[Integer]|6|Maximum depth of a tree. Increasing this value will make the model more complex and more likely to overfit.<br/>0 indicates no limit on depth. Range: [0,Inf].|
|booster_params|[JsonObject]||Parameters for the booster. See https://xgboost.readthedocs.io/en/latest/parameter.html|

## Outputs

|Name|Type|Description|
|-|-|-|
|model|[XGBoostModel]|Trained model in the binary XGBoost format.|
|model_config|[XGBoostModelConfig]|The internal parameter configuration of Booster as a JSON string.|

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
train_XGBoost_model_on_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/XGBoost/Train/component.yaml")
...
train_XGBoost_model_on_CSV_task = train_XGBoost_model_on_CSV_op(
    training_data=...,
    label_column_name=...,
    # Optional:
    # starting_model=...,
    # num_iterations=10,
    # objective="reg:squarederror",
    # booster="gbtree",
    # learning_rate=0.3,
    # min_split_loss=0.0,
    # max_depth=6,
    # booster_params={...},
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[Float]
* input_type=[Integer]
* input_type=[JsonObject]
* input_type=[String]
* input_type=[XGBoostModel]
* output_type=[XGBoostModel]
* output_type=[XGBoostModelConfig]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[XGBoostModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/XGBoostModel
[XGBoostModelConfig]: https://github.com/Ark-kun/pipeline_components/tree/master/types/XGBoostModelConfig
<!-- END_GENERATED_CONTENT -->
