<!-- BEGIN_GENERATED_CONTENT -->
# Train tabular model using Google Cloud Vertex AI AutoML

Description: Trains model using Google Cloud Vertex AI AutoML.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Vertex_AI/AutoML/Tables/Train_model/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/AutoML/Tables/Train_model/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dataset_name** **\***|[GoogleCloudVertexAiTabularDatasetName]||Required. The full name of dataset  (datasets.TabularDataset) within the same Project from which data will be used to train the Model. The<br/>Dataset must use schema compatible with Model being trained,<br/>and what is compatible should be described in the used<br/>TrainingPipeline's [training_task_definition]<br/>[google.cloud.aiplatform.v1beta1.TrainingPipeline.training_task_definition].<br/>For tabular Datasets, all their data is exported to<br/>training, to pick and choose from.|
|**target_column** **\***|[String]||Required. The name of the column values of which the Model is to predict.|
|**optimization_prediction_type** **\***|[String]||The type of prediction the Model is to produce.<br/>"classification" - Predict one out of multiple target values is<br/>picked for each row.<br/>"regression" - Predict a value based on its relation to other values.<br/>This type is available only to columns that contain<br/>semantically numeric values, i.e. integers or floating<br/>point number, even if stored as e.g. strings.|
|training_fraction_split|[Float]|0.8|Required. The fraction of the input data that is to be<br/>used to train the Model. This is ignored if Dataset is not provided.|
|validation_fraction_split|[Float]|0.1|Required. The fraction of the input data that is to be<br/>used to validate the Model. This is ignored if Dataset is not provided.|
|test_fraction_split|[Float]|0.1|Required. The fraction of the input data that is to be<br/>used to evaluate the Model. This is ignored if Dataset is not provided.|
|predefined_split_column_name|[String]||Optional. The key is a name of one of the Dataset's data<br/>columns. The value of the key (either the label's value or<br/>value in the column) must be one of {``training``,<br/>``validation``, ``test``}, and it defines to which set the<br/>given piece of data is assigned. If for a piece of data the<br/>key is not present or has an invalid value, that piece is<br/>ignored by the pipeline.<br/><br/>Supported only for tabular and time series Datasets.|
|weight_column|[String]||Optional. Name of the column that should be used as the weight column.<br/>Higher values in this column give more importance to the row<br/>during Model training. The column must have numeric values between 0 and<br/>10000 inclusively, and 0 value means that the row is ignored.<br/>If the weight column field is not set, then all rows are assumed to have<br/>equal weight of 1.|
|budget_milli_node_hours|[Integer]|1000|Optional. The train budget of creating this Model, expressed in milli node<br/>hours i.e. 1,000 value in this field means 1 node hour.<br/>The training cost of the model will not exceed this budget. The final<br/>cost will be attempted to be close to the budget, though may end up<br/>being (even) noticeably smaller - at the backend's discretion. This<br/>especially may happen when further model training ceases to provide<br/>any improvements.<br/>If the budget is set to a value known to be insufficient to train a<br/>Model for the given training set, the training won't be attempted and<br/>will error.<br/>The minimum value is 1000 and the maximum is 72000.|
|model_display_name|[String]||Optional. If the script produces a managed Vertex AI Model. The display name of<br/>the Model. The name can be up to 128 characters long and can be consist<br/>of any UTF-8 characters.<br/><br/>If not provided upon creation, the job's display_name is used.|
|disable_early_stopping|[Boolean]|False|Required. If true, the entire budget is used. This disables the early stopping<br/>feature. By default, the early stopping feature is enabled, which means<br/>that training might stop before the entire training budget has been<br/>used, if further training does no longer brings significant improvement<br/>to the model.|
|optimization_objective|[String]||Optional. Objective function the Model is to be optimized towards. The training<br/>task creates a Model that maximizes/minimizes the value of the objective<br/>function over the validation set.<br/><br/>The supported optimization objectives depend on the prediction type, and<br/>in the case of classification also the number of distinct values in the<br/>target column (two distint values -> binary, 3 or more distinct values<br/>-> multi class).<br/>If the field is not set, the default objective function is used.<br/><br/>Classification (binary):<br/>"maximize-au-roc" (default) - Maximize the area under the receiver<br/>                            operating characteristic (ROC) curve.<br/>"minimize-log-loss" - Minimize log loss.<br/>"maximize-au-prc" - Maximize the area under the precision-recall curve.<br/>"maximize-precision-at-recall" - Maximize precision for a specified<br/>                                recall value.<br/>"maximize-recall-at-precision" - Maximize recall for a specified<br/>                                precision value.<br/><br/>Classification (multi class):<br/>"minimize-log-loss" (default) - Minimize log loss.<br/><br/>Regression:<br/>"minimize-rmse" (default) - Minimize root-mean-squared error (RMSE).<br/>"minimize-mae" - Minimize mean-absolute error (MAE).<br/>"minimize-rmsle" - Minimize root-mean-squared log error (RMSLE).|
|optimization_objective_recall_value|[Float]||Optional. Required when maximize-precision-at-recall optimizationObjective was<br/>picked, represents the recall value at which the optimization is done.<br/><br/>The minimum value is 0 and the maximum is 1.0.|
|optimization_objective_precision_value|[Float]||Optional. Required when maximize-recall-at-precision optimizationObjective was<br/>picked, represents the precision value at which the optimization is<br/>done.<br/><br/>The minimum value is 0 and the maximum is 1.0.|
|project|[String]|||
|location|[String]|us-central1||
|encryption_spec_key_name|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|model_name|[GoogleCloudVertexAiModelName]||
|model_dict|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
train_tabular_model_using_Google_Cloud_Vertex_AI_AutoML_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/AutoML/Tables/Train_model/component.yaml")
...
train_tabular_model_using_Google_Cloud_Vertex_AI_AutoML_task = train_tabular_model_using_Google_Cloud_Vertex_AI_AutoML_op(
    dataset_name=...,
    target_column=...,
    optimization_prediction_type=...,
    # Optional:
    # training_fraction_split=0.8,
    # validation_fraction_split=0.1,
    # test_fraction_split=0.1,
    # predefined_split_column_name=...,
    # weight_column=...,
    # budget_milli_node_hours=1000,
    # model_display_name=...,
    # disable_early_stopping=False,
    # optimization_objective=...,
    # optimization_objective_recall_value=...,
    # optimization_objective_precision_value=...,
    # project=...,
    # location="us-central1",
    # encryption_spec_key_name=...,
)
```

## Other information

###### Tags

* input_type=[Boolean]
* input_type=[Float]
* input_type=[GoogleCloudVertexAiTabularDatasetName]
* input_type=[Integer]
* input_type=[String]
* output_type=[GoogleCloudVertexAiModelName]
* output_type=[JsonObject]

[Boolean]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Boolean
[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[GoogleCloudVertexAiModelName]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GoogleCloudVertexAiModelName
[GoogleCloudVertexAiTabularDatasetName]: https://github.com/Ark-kun/pipeline_components/tree/master/types/GoogleCloudVertexAiTabularDatasetName
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
