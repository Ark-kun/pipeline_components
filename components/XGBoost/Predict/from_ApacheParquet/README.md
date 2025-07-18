<!-- BEGIN_GENERATED_CONTENT -->
# Xgboost predict on ApacheParquet

Description: Makes predictions using a trained XGBoost model.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/XGBoost/Predict/from_ApacheParquet/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/XGBoost/Predict/from_ApacheParquet/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data** **\***|[ApacheParquet]||Feature data in Apache Parquet format.|
|**model** **\***|[XGBoostModel]||Trained model in binary XGBoost format.|
|label_column_name|[String]||Optional. Name of the column containing the label data that is excluded during the prediction.|

## Outputs

|Name|Type|Description|
|-|-|-|
|predictions||Model predictions.|

## Implementation

#### Container

Container image: [python:3.10](https://hub.docker.com/r/_/python)

## Usage

```python
xgboost_predict_on_ApacheParquet_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/XGBoost/Predict/from_ApacheParquet/component.yaml")
...
xgboost_predict_on_ApacheParquet_task = xgboost_predict_on_ApacheParquet_op(
    data=...,
    model=...,
    # Optional:
    # label_column_name=...,
)
```

## Other information

###### Tags

* input_type=[ApacheParquet]
* input_type=[String]
* input_type=[XGBoostModel]

[ApacheParquet]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ApacheParquet
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[XGBoostModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/XGBoostModel
<!-- END_GENERATED_CONTENT -->
