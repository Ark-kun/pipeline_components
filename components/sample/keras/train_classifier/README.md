<!-- BEGIN_GENERATED_CONTENT -->
# Keras - Train classifier

Description: Trains classifier using Keras sequential model

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/sample/keras/train_classifier/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/sample/keras/train_classifier/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**training_set_features_path** **\***|[GcsPath]: `{"data_type": "TSV"}`||Local or GCS path to the training set features table.|
|**training_set_labels_path** **\***|[GcsPath]: `{"data_type": "TSV"}`||Local or GCS path to the training set labels (each label is a class index from 0 to num-classes - 1).|
|**output_model_uri** **\***|[GcsPath]: `{"data_type": "Keras model"}`||Local or GCS path specifying where to save the trained model. The model (topology + weights + optimizer state) is saved in HDF5 format and can be loaded back by calling keras.models.load_model|
|**model_config** **\***|[GcsPath]: `{"data_type": "Keras model config json"}`||JSON string containing the serialized model structure. Can be obtained by calling model.to_json() on a Keras model.|
|**number_of_classes** **\***|[Integer]||Number of classifier classes.|
|**number_of_epochs** **\***|[Integer]|100|Number of epochs to train the model. An epoch is an iteration over the entire `x` and `y` data provided.|
|**batch_size** **\***|[Integer]|32|Number of samples per gradient update.|

## Outputs

|Name|Type|Description|
|-|-|-|
|output_model_uri|[GcsPath]: `{"data_type": "Keras model"}`|GCS path where the trained model has been saved. The model (topology + weights + optimizer state) is saved in HDF5 format and can be loaded back by calling keras.models.load_model|

## Implementation

#### Container

Container image: [gcr.io/ml-pipeline/sample/keras/train_classifier](gcr.io/ml-pipeline/sample/keras/train_classifier)

## Usage

```python
keras_Train_classifier_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/sample/keras/train_classifier/component.yaml")
...
keras_Train_classifier_task = keras_Train_classifier_op(
    training_set_features_path=...,
    training_set_labels_path=...,
    output_model_uri=...,
    model_config=...,
    number_of_classes=...,
    number_of_epochs=...,
    batch_size=...,
)
```

## Other information

###### Tags

* input_type=[GcsPath]
* input_type=[Integer]
* output_type=[GcsPath]

[GcsPath]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GcsPath
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
<!-- END_GENERATED_CONTENT -->
