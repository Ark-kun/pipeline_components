<!-- BEGIN_GENERATED_CONTENT -->
# Xgboost train and cv regression on csv

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/XGBoost/Train_and_cross-validate_regression/from_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/XGBoost/Train_and_cross-validate_regression/from_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data** **\***|[CSV]|||
|label_column|[Integer]|0||
|objective|[String]|reg:squarederror||
|num_iterations|[Integer]|200||

## Outputs

|Name|Type|Description|
|-|-|-|
|model|[XGBoostModel]||
|training_mean_absolute_error|[Float]||
|training_mean_squared_error|[Float]||
|training_root_mean_squared_error|[Float]||
|training_metrics|[JsonObject]||
|cv_mean_absolute_error|[Float]||
|cv_mean_squared_error|[Float]||
|cv_root_mean_squared_error|[Float]||
|cv_metrics|[JsonObject]||

## Implementation

#### Graph

##### Tasks

*   Task "Xgboost train": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml)
*   Task "Xgboost predict": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml)
*   Task "Pandas Transform DataFrame in CSV format": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml)
*   Task "Remove header": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml)
*   Task "Calculate regression metrics from csv": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml)
*   Task "Split table into folds": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/dataset_manipulation/split_data_into_folds/in_CSV/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/dataset_manipulation/split_data_into_folds/in_CSV/component.yaml)
*   Task "Xgboost train 2": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml)
*   Task "Xgboost predict 2": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml)
*   Task "Pandas Transform DataFrame in CSV format 2": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml)
*   Task "Remove header 2": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml)
*   Task "Calculate regression metrics from csv 2": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml)
*   Task "Xgboost train 3": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml)
*   Task "Xgboost predict 3": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml)
*   Task "Pandas Transform DataFrame in CSV format 3": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml)
*   Task "Remove header 3": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml)
*   Task "Calculate regression metrics from csv 3": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml)
*   Task "Xgboost train 4": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml)
*   Task "Xgboost predict 4": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml)
*   Task "Pandas Transform DataFrame in CSV format 4": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml)
*   Task "Remove header 4": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml)
*   Task "Calculate regression metrics from csv 4": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml)
*   Task "Xgboost train 5": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml)
*   Task "Xgboost predict 5": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml)
*   Task "Pandas Transform DataFrame in CSV format 5": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml)
*   Task "Remove header 5": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml)
*   Task "Calculate regression metrics from csv 5": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml)
*   Task "Xgboost train 6": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml)
*   Task "Xgboost predict 6": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml)
*   Task "Pandas Transform DataFrame in CSV format 6": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml)
*   Task "Remove header 6": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml)
*   Task "Calculate regression metrics from csv 6": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml)
*   Task "Aggregate regression metrics": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Aggregate_regression_metrics/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Aggregate_regression_metrics/component.yaml)

## Usage

```python
xgboost_train_and_cv_regression_on_csv_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/XGBoost/Train_and_cross-validate_regression/from_CSV/component.yaml")
...
xgboost_train_and_cv_regression_on_csv_task = xgboost_train_and_cv_regression_on_csv_op(
    data=...,
    # Optional:
    # label_column=0,
    # objective="reg:squarederror",
    # num_iterations=200,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[Integer]
* input_type=[String]
* output_type=[Float]
* output_type=[JsonObject]
* output_type=[XGBoostModel]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[XGBoostModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/XGBoostModel
<!-- END_GENERATED_CONTENT -->
