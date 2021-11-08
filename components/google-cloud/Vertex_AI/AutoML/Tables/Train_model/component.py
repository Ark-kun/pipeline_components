from typing import NamedTuple

from kfp.components import create_component_from_func

def train_tabular_model_using_Google_Cloud_Vertex_AI_AutoML(
    # AutoMLTabularTrainingJob.run required parameters
    dataset_name: 'GoogleCloudVertexAiTabularDatasetName',
    target_column: str,

    # AutoMLTabularTrainingJob.__init__ required parameters
    # display_name: str,
    optimization_prediction_type: str,

    # AutoMLTabularTrainingJob.run parameters
    training_fraction_split: float = 0.8,
    validation_fraction_split: float = 0.1,
    test_fraction_split: float = 0.1,
    predefined_split_column_name: str = None,
    weight_column: str = None,
    budget_milli_node_hours: int = 1000,
    model_display_name: str = None,
    disable_early_stopping: bool = False,

    # AutoMLTabularTrainingJob.__init__ parameters
    optimization_objective: str = None,
    #column_transformations: Union[Dict, List[Dict], NoneType] = None,
    optimization_objective_recall_value: float = None,
    optimization_objective_precision_value: float = None,

    project: str = None,
    location: str = 'us-central1',
    #training_encryption_spec_key_name: str = None,
    #model_encryption_spec_key_name: str = None,
    encryption_spec_key_name: str = None,
) -> NamedTuple('Outputs', [
    ('model_name', 'GoogleCloudVertexAiModelName'),
    ('model_dict', dict),
]):
    '''Trains model using Google Cloud Vertex AI AutoML.

    Data fraction splits:
    Any of ``training_fraction_split``, ``validation_fraction_split`` and
    ``test_fraction_split`` may optionally be provided, they must sum to up to 1. If
    the provided ones sum to less than 1, the remainder is assigned to sets as
    decided by Vertex AI. If none of the fractions are set, by default roughly 80%
    of data will be used for training, 10% for validation, and 10% for test.

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

    Args:
        dataset_name:
            Required. The full name of dataset  (datasets.TabularDataset) within the same Project from which data will be used to train the Model. The
            Dataset must use schema compatible with Model being trained,
            and what is compatible should be described in the used
            TrainingPipeline's [training_task_definition]
            [google.cloud.aiplatform.v1beta1.TrainingPipeline.training_task_definition].
            For tabular Datasets, all their data is exported to
            training, to pick and choose from.
        target_column (str):
            Required. The name of the column values of which the Model is to predict.
        training_fraction_split (float):
            Required. The fraction of the input data that is to be
            used to train the Model. This is ignored if Dataset is not provided.
        validation_fraction_split (float):
            Required. The fraction of the input data that is to be
            used to validate the Model. This is ignored if Dataset is not provided.
        test_fraction_split (float):
            Required. The fraction of the input data that is to be
            used to evaluate the Model. This is ignored if Dataset is not provided.
        predefined_split_column_name (str):
            Optional. The key is a name of one of the Dataset's data
            columns. The value of the key (either the label's value or
            value in the column) must be one of {``training``,
            ``validation``, ``test``}, and it defines to which set the
            given piece of data is assigned. If for a piece of data the
            key is not present or has an invalid value, that piece is
            ignored by the pipeline.

            Supported only for tabular and time series Datasets.
        weight_column (str):
            Optional. Name of the column that should be used as the weight column.
            Higher values in this column give more importance to the row
            during Model training. The column must have numeric values between 0 and
            10000 inclusively, and 0 value means that the row is ignored.
            If the weight column field is not set, then all rows are assumed to have
            equal weight of 1.
        budget_milli_node_hours (int):
            Optional. The train budget of creating this Model, expressed in milli node
            hours i.e. 1,000 value in this field means 1 node hour.
            The training cost of the model will not exceed this budget. The final
            cost will be attempted to be close to the budget, though may end up
            being (even) noticeably smaller - at the backend's discretion. This
            especially may happen when further model training ceases to provide
            any improvements.
            If the budget is set to a value known to be insufficient to train a
            Model for the given training set, the training won't be attempted and
            will error.
            The minimum value is 1000 and the maximum is 72000.
        model_display_name (str):
            Optional. If the script produces a managed Vertex AI Model. The display name of
            the Model. The name can be up to 128 characters long and can be consist
            of any UTF-8 characters.

            If not provided upon creation, the job's display_name is used.
        disable_early_stopping (bool):
            Required. If true, the entire budget is used. This disables the early stopping
            feature. By default, the early stopping feature is enabled, which means
            that training might stop before the entire training budget has been
            used, if further training does no longer brings significant improvement
            to the model.

        optimization_prediction_type (str):
            The type of prediction the Model is to produce.
            "classification" - Predict one out of multiple target values is
            picked for each row.
            "regression" - Predict a value based on its relation to other values.
            This type is available only to columns that contain
            semantically numeric values, i.e. integers or floating
            point number, even if stored as e.g. strings.
        optimization_objective (str):
            Optional. Objective function the Model is to be optimized towards. The training
            task creates a Model that maximizes/minimizes the value of the objective
            function over the validation set.

            The supported optimization objectives depend on the prediction type, and
            in the case of classification also the number of distinct values in the
            target column (two distint values -> binary, 3 or more distinct values
            -> multi class).
            If the field is not set, the default objective function is used.

            Classification (binary):
            "maximize-au-roc" (default) - Maximize the area under the receiver
                                        operating characteristic (ROC) curve.
            "minimize-log-loss" - Minimize log loss.
            "maximize-au-prc" - Maximize the area under the precision-recall curve.
            "maximize-precision-at-recall" - Maximize precision for a specified
                                            recall value.
            "maximize-recall-at-precision" - Maximize recall for a specified
                                            precision value.

            Classification (multi class):
            "minimize-log-loss" (default) - Minimize log loss.

            Regression:
            "minimize-rmse" (default) - Minimize root-mean-squared error (RMSE).
            "minimize-mae" - Minimize mean-absolute error (MAE).
            "minimize-rmsle" - Minimize root-mean-squared log error (RMSLE).
        column_transformations (Optional[Union[Dict, List[Dict]]]):
            Optional. Transformations to apply to the input columns (i.e. columns other
            than the targetColumn). Each transformation may produce multiple
            result values from the column's value, and all are used for training.
            When creating transformation for BigQuery Struct column, the column
            should be flattened using "." as the delimiter.
            If an input column has no transformations on it, such a column is
            ignored by the training, except for the targetColumn, which should have
            no transformations defined on.
        optimization_objective_recall_value (float):
            Optional. Required when maximize-precision-at-recall optimizationObjective was
            picked, represents the recall value at which the optimization is done.

            The minimum value is 0 and the maximum is 1.0.
        optimization_objective_precision_value (float):
            Optional. Required when maximize-recall-at-precision optimizationObjective was
            picked, represents the precision value at which the optimization is
            done.

            The minimum value is 0 and the maximum is 1.0.

    Returns:
        model_name: Model name (fully-qualified)
        model_dict: Model metadata in JSON format
    '''

    import datetime
    import logging
    import os

    from google.cloud import aiplatform
    from google.protobuf import json_format

    logging.getLogger().setLevel(logging.INFO)

    if not model_display_name:
        model_display_name = 'TablesModel_' + datetime.datetime.utcnow().strftime("%Y_%m_%d_%H_%M_%S")

    # Problem: Unlike KFP, when running on Vertex AI, google.auth.default() returns incorrect GCP project ID.
    # This leads to failure when trying to create any resource in the project.
    # google.api_core.exceptions.PermissionDenied: 403 Permission 'aiplatform.models.upload' denied on resource '//aiplatform.googleapis.com/projects/gbd40bc90c7804989-tp/locations/us-central1' (or it may not exist).
    # We can try and get the GCP project ID/number from the environment variables.
    if not project:
        project_number = os.environ.get("CLOUD_ML_PROJECT_ID")
        if project_number:
            print(f"Inferred project number: {project_number}")
            project = project_number
            # To improve the naming we try to convert the project number into the user project ID.
            try:
                from googleapiclient import discovery

                cloud_resource_manager_service = discovery.build(
                    "cloudresourcemanager", "v3"
                )
                project_id = (
                    cloud_resource_manager_service.projects()
                    .get(name=f"projects/{project_number}")
                    .execute()["projectId"]
                )
                if project_id:
                    print(f"Inferred project ID: {project_id}")
                    project = project_id
            except Exception as e:
                print(e)

    aiplatform.init(
        project=project,
        location=location,
        encryption_spec_key_name=encryption_spec_key_name,
    )
    
    model = aiplatform.AutoMLTabularTrainingJob(
        display_name='AutoMLTabularTrainingJob_' + datetime.datetime.utcnow().strftime("%Y_%m_%d_%H_%M_%S"),
        optimization_prediction_type=optimization_prediction_type,
        optimization_objective=optimization_objective,
        #column_transformations=column_transformations,
        optimization_objective_recall_value=optimization_objective_recall_value,
        optimization_objective_precision_value=optimization_objective_precision_value,
    ).run(
        dataset=aiplatform.TabularDataset(dataset_name=dataset_name),
        target_column=target_column,
        training_fraction_split=training_fraction_split,
        validation_fraction_split=validation_fraction_split,
        test_fraction_split=test_fraction_split,
        predefined_split_column_name=predefined_split_column_name,
        weight_column=weight_column,
        budget_milli_node_hours=budget_milli_node_hours,
        model_display_name=model_display_name,
        disable_early_stopping=disable_early_stopping,
    )

    (_, model_project, _, model_location, _, model_id) = model.resource_name.split('/')
    model_web_url = f'https://console.cloud.google.com/vertex-ai/locations/{model_location}/models/{model_id}/evaluate?project={model_project}'
    logging.info(f'Created model {model.name}.')
    logging.info(f'Link: {model_web_url}')
    model_json = json_format.MessageToJson(model._gca_resource._pb)
    print(model_json)
    return (model.resource_name, model_json, model_web_url)


if __name__ == '__main__':
    train_tabular_model_using_Google_Cloud_Vertex_AI_AutoML_op = create_component_from_func(
        train_tabular_model_using_Google_Cloud_Vertex_AI_AutoML,
        base_image='python:3.9',
        packages_to_install=[
            "google-cloud-aiplatform==1.6.2",
            "google-api-python-client==2.29.0",  # For project number -> project ID conversion
        ],
        output_component_file='component.yaml',
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Vertex_AI/AutoML/Tables/Train_model/component.yaml",
        },
    )
