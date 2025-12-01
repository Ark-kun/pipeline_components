<!-- BEGIN_GENERATED_CONTENT -->
# Predict with PyTorch model on ApacheParquet data

Description: Makes predictions using a trained PyTorch model.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/PyTorch/Predict/on_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/PyTorch/Predict/on_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**data** **\***|[ApacheParquet]||Feature data in CSV format.|
|**model** **\***|[PyTorchScriptModule]||Trained model in binary PyTorchScriptModule format.|
|label_column_name|[String]||Optional. Name of the column containing the label data that is excluded during the prediction.|
|prediction_column_name|[String]|prediction||
|batch_size|[Integer]|100||

## Outputs

|Name|Type|Description|
|-|-|-|
|predictions|[ApacheParquet]|Model predictions.|

## Implementation

#### Container

Container image: [pytorch/pytorch:1.7.1-cuda11.0-cudnn8-runtime](https://hub.docker.com/r/pytorch/pytorch)

## Usage

```python
predict_with_PyTorch_model_on_ApacheParquet_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/PyTorch/Predict/on_CSV/component.yaml")
...
predict_with_PyTorch_model_on_ApacheParquet_data_task = predict_with_PyTorch_model_on_ApacheParquet_data_op(
    data=...,
    model=...,
    # Optional:
    # label_column_name=...,
    # prediction_column_name="prediction",
    # batch_size=100,
)
```

## Other information

###### Tags

* input_type=[ApacheParquet]
* input_type=[Integer]
* input_type=[PyTorchScriptModule]
* input_type=[String]
* output_type=[ApacheParquet]

[ApacheParquet]: https://github.com/Ark-kun/pipeline_components/tree/master/types/ApacheParquet
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[PyTorchScriptModule]: https://github.com/Ark-kun/pipeline_components/tree/master/types/PyTorchScriptModule
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
