<!-- BEGIN_GENERATED_CONTENT -->
# Catboost predict values

Description: Predict values with a CatBoost model.

    Args:
        data_path: Path for the data in CSV format.
        model_path: Path for the trained model in binary CatBoostModel format.
        label_column: Column containing the label data.
        predictions_path: Output path for the predictions.

    Outputs:
        predictions: Predictions in text format.

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/CatBoost/Predict_values/from_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/CatBoost/Predict_values/from_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data** **\***|[CSV]|||
|**model** **\***|[CatBoostModel]|||
|label_column|[Integer]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|predictions|||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
catboost_predict_values_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/CatBoost/Predict_values/from_CSV/component.yaml")
...
catboost_predict_values_task = catboost_predict_values_op(
    data=...,
    model=...,
    # Optional:
    # label_column=...,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[CatBoostModel]
* input_type=[Integer]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[CatBoostModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CatBoostModel
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
<!-- END_GENERATED_CONTENT -->
