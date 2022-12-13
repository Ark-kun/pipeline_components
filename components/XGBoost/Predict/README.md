<!-- BEGIN_GENERATED_CONTENT -->
# Xgboost predict on CSV

Description: Makes predictions using a trained XGBoost model.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/XGBoost/Predict/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/XGBoost/Predict/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data** **\***|[CSV]||Feature data in Apache Parquet format.|
|**model** **\***|[XGBoostModel]||Trained model in binary XGBoost format.|
|label_column_name|[String]||Optional. Name of the column containing the label data that is excluded during the prediction.|

## Outputs

|Name|Type|Description|
|-|-|-|
|predictions|[Text]|Model predictions.|

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
xgboost_predict_on_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/XGBoost/Predict/component.yaml")
...
xgboost_predict_on_CSV_task = xgboost_predict_on_CSV_op(
    data=...,
    model=...,
    # Optional:
    # label_column_name=...,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[String]
* input_type=[XGBoostModel]
* output_type=[Text]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[Text]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Text
[XGBoostModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/XGBoostModel
<!-- END_GENERATED_CONTENT -->
