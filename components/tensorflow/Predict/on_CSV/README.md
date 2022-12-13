<!-- BEGIN_GENERATED_CONTENT -->
# Predict with TensorFlow model on CSV data

Description: Makes predictions using TensorFlow model.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/tensorflow/Predict/on_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/tensorflow/Predict/on_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dataset** **\***|[CSV]||Tabular dataset for prediction.|
|**model** **\***|[TensorflowSavedModel]||Trained model in TensorFlow format.|
|label_column_name|[String]||Name of the table column to use as label.|
|batch_size|[Integer]|1000|Number of samples to use in each batch.|

## Outputs

|Name|Type|Description|
|-|-|-|
|predictions||Predictions in multiline text format.|

## Implementation

#### Container

Container image: [tensorflow/tensorflow:2.9.1](https://hub.docker.com/r/tensorflow/tensorflow)

## Usage

```python
predict_with_TensorFlow_model_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/tensorflow/Predict/on_CSV/component.yaml")
...
predict_with_TensorFlow_model_on_CSV_data_task = predict_with_TensorFlow_model_on_CSV_data_op(
    dataset=...,
    model=...,
    # Optional:
    # label_column_name=...,
    # batch_size=1000,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[Integer]
* input_type=[String]
* input_type=[TensorflowSavedModel]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[TensorflowSavedModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TensorflowSavedModel
<!-- END_GENERATED_CONTENT -->
