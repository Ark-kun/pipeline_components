<!-- BEGIN_GENERATED_CONTENT -->
# Train pytorch model from csv

Description: Trains PyTorch model.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/PyTorch/Train_PyTorch_model/from_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/PyTorch/Train_PyTorch_model/from_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[PyTorchScriptModule]||Model in PyTorch format.|
|**training_data** **\***|[CSV]||Tabular dataset for training.|
|**label_column_name** **\***|[String]||Name of the table column to use as label.|
|loss_function_name|[String]|mse_loss|Name of the loss function.|
|number_of_epochs|[Integer]|1|Number of training epochs.|
|learning_rate|[Float]|0.1|Learning rate of the optimizer.|
|optimizer_name|[String]|Adadelta|Name of the optimizer.|
|optimizer_parameters|[JsonObject]||Optimizer parameters in dictionary form.|
|batch_size|[Integer]|32|Number of training samples to use in each batch.|
|batch_log_interval|[Integer]|100|Print training summary after every N batches.|
|random_seed|[Integer]|0|Controls the seed of the random processes.|

## Outputs

|Name|Type|Description|
|-|-|-|
|trained_model|[PyTorchScriptModule]|Trained model in PyTorch format.|

## Implementation

#### Container

Container image: [pytorch/pytorch:1.7.1-cuda11.0-cudnn8-runtime](https://hub.docker.com/r/pytorch/pytorch)

## Usage

```python
train_pytorch_model_from_csv_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/PyTorch/Train_PyTorch_model/from_CSV/component.yaml")
...
train_pytorch_model_from_csv_task = train_pytorch_model_from_csv_op(
    model=...,
    training_data=...,
    label_column_name=...,
    # Optional:
    # loss_function_name="mse_loss",
    # number_of_epochs=1,
    # learning_rate=0.1,
    # optimizer_name="Adadelta",
    # optimizer_parameters={...},
    # batch_size=32,
    # batch_log_interval=100,
    # random_seed=0,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[Float]
* input_type=[Integer]
* input_type=[JsonObject]
* input_type=[PyTorchScriptModule]
* input_type=[String]
* output_type=[PyTorchScriptModule]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[PyTorchScriptModule]: https://github.com/Ark-kun/pipeline_components/tree/master/types/PyTorchScriptModule
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
