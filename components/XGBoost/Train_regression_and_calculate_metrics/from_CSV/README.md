<!-- BEGIN_GENERATED_CONTENT -->
# Xgboost train regression and calculate metrics on csv

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/XGBoost/Train_regression_and_calculate_metrics/from_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/XGBoost/Train_regression_and_calculate_metrics/from_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**training_data** **\***|[CSV]|||
|**testing_data** **\***|[CSV]|||
|label_column|[Integer]|0||
|objective|[String]|reg:squarederror||
|num_iterations|[Integer]|200||

## Outputs

|Name|Type|Description|
|-|-|-|
|model|[XGBoostModel]||
|mean_absolute_error|[Float]||
|mean_squared_error|[Float]||
|root_mean_squared_error|[Float]||
|metrics|[JsonObject]||

## Implementation

#### Graph

##### Tasks

*   Task "Xgboost train": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml)
*   Task "Xgboost predict": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml)
*   Task "Pandas Transform DataFrame in CSV format": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml)
*   Task "Remove header": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml)
*   Task "Calculate regression metrics from csv": Component [Web URL](https://github.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml), [Raw URL](https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml)

## Usage

```python
xgboost_train_regression_and_calculate_metrics_on_csv_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/XGBoost/Train_regression_and_calculate_metrics/from_CSV/component.yaml")
...
xgboost_train_regression_and_calculate_metrics_on_csv_task = xgboost_train_regression_and_calculate_metrics_on_csv_op(
    training_data=...,
    testing_data=...,
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
