<!-- BEGIN_GENERATED_CONTENT -->
# Train model using Keras on CSV

Description: Trains TensorFlow model.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/tensorflow/Train_model_using_Keras/on_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/tensorflow/Train_model_using_Keras/on_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**training_data** **\***|[CSV]||Tabular dataset for training.|
|**model** **\***|[TensorflowSavedModel]||Model in TensorFlow format.|
|**label_column_name** **\***|[String]||Name of the table column to use as label.|
|loss_function_name|[String]|mean_squared_error|Name of the loss function.|
|number_of_epochs|[Integer]|1|Number of training epochs.|
|learning_rate|[Float]|0.1|Learning rate of the optimizer.|
|optimizer_name|[String]|Adadelta|Name of the optimizer.|
|optimizer_parameters|[JsonObject]||Optimizer parameters in dictionary form.|
|batch_size|[Integer]|32|Number of training samples to use in each batch.|
|metric_names|[JsonArray]||A list of metrics to evaluate during the training.|
|random_seed|[Integer]|0|Controls the seed of the random processes.|

## Outputs

|Name|Type|Description|
|-|-|-|
|trained_model|[TensorflowSavedModel]|Trained model in TensorFlow format.|

## Implementation

#### Container

Container image: [tensorflow/tensorflow:2.8.0](https://hub.docker.com/r/tensorflow/tensorflow)

## Usage

```python
train_model_using_Keras_on_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/tensorflow/Train_model_using_Keras/on_CSV/component.yaml")
...
train_model_using_Keras_on_CSV_task = train_model_using_Keras_on_CSV_op(
    training_data=...,
    model=...,
    label_column_name=...,
    # Optional:
    # loss_function_name="mean_squared_error",
    # number_of_epochs=1,
    # learning_rate=0.1,
    # optimizer_name="Adadelta",
    # optimizer_parameters={...},
    # batch_size=32,
    # metric_names=[...],
    # random_seed=0,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[Float]
* input_type=[Integer]
* input_type=[JsonArray]
* input_type=[JsonObject]
* input_type=[String]
* input_type=[TensorflowSavedModel]
* output_type=[TensorflowSavedModel]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[TensorflowSavedModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/TensorflowSavedModel
<!-- END_GENERATED_CONTENT -->
