<!-- BEGIN_GENERATED_CONTENT -->
# Keras train classifier from csv

Description: Trains classifier model using Keras.

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/keras/Train_classifier/from_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/keras/Train_classifier/from_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**training_features** **\***|[CSV]|||
|**training_labels** **\***|[CSV]|||
|**network_json** **\***|[KerasModelJson]|||
|loss_name|[String]|categorical_crossentropy||
|num_classes|[Integer]|||
|optimizer|[String]|rmsprop||
|optimizer_config|[JsonObject]|||
|learning_rate|[Float]|0.01||
|num_epochs|[Integer]|100||
|batch_size|[Integer]|32||
|metrics|[JsonArray]|["accuracy"]||
|random_seed|[Integer]|0||

## Outputs

|Name|Type|Description|
|-|-|-|
|model|[KerasModelHdf5]||
|final_loss|[Float]||
|final_metrics|[JsonObject]||
|metrics_history|[JsonObject]||

## Implementation

#### Container

Container image: [tensorflow/tensorflow:2.2.0](https://hub.docker.com/r/tensorflow/tensorflow)

## Usage

```python
keras_train_classifier_from_csv_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/keras/Train_classifier/from_CSV/component.yaml")
...
keras_train_classifier_from_csv_task = keras_train_classifier_from_csv_op(
    training_features=...,
    training_labels=...,
    network_json=...,
    # Optional:
    # loss_name="categorical_crossentropy",
    # num_classes=...,
    # optimizer="rmsprop",
    # optimizer_config={...},
    # learning_rate=0.01,
    # num_epochs=100,
    # batch_size=32,
    # metrics="["accuracy"]",
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
* input_type=[KerasModelJson]
* input_type=[String]
* output_type=[Float]
* output_type=[JsonObject]
* output_type=[KerasModelHdf5]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[KerasModelHdf5]: https://github.com/Ark-kun/pipeline_components/tree/master/types/KerasModelHdf5
[KerasModelJson]: https://github.com/Ark-kun/pipeline_components/tree/master/types/KerasModelJson
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
