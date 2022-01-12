# This sample demonstrates a common training scenario.
# New models are being trained strarting from the production model (if it exists).
# This sample produces two runs:
# 1. The trainer will train the model from scratch and set as prod after testing it
# 2. Exact same configuration, but the pipeline will discover the existing prod model (published by the 1st run) and warm-start the training from it.


# GCS URI of a directory where the models and the model pointers should be be stored.
model_dir_uri='gs://<bucket>/<path>'
kfp_endpoint=None


import kfp
from kfp import components


chicago_taxi_dataset_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/datasets/Chicago_Taxi_Trips/component.yaml')
xgboost_train_on_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml')
xgboost_predict_on_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml')

pandas_transform_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml')
drop_header_op = kfp.components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml')
calculate_regression_metrics_from_csv_op = kfp.components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml')

download_from_gcs_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/google-cloud/storage/download/component.yaml')
upload_to_gcs_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/6210648f30b2b3a8c01cc10be338da98300efb6b/components/google-cloud/storage/upload_to_explicit_uri/component.yaml')
upload_to_gcs_unique_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/6210648f30b2b3a8c01cc10be338da98300efb6b/components/google-cloud/storage/upload_to_unique_uri/component.yaml')


def continuous_training_pipeline(
    model_dir_uri,
    training_start_date: str = '2019-02-01',
    training_end_date: str = '2019-03-01',
    testing_start_date: str = '2019-01-01',
    testing_end_date: str = '2019-02-01',
):
    # Preparing the training and testing data
    training_data = chicago_taxi_dataset_op(
        where='trip_start_timestamp >= "{}" AND trip_start_timestamp < "{}"'.format(str(training_start_date), str(training_end_date)),
        select='tips,trip_seconds,trip_miles,pickup_community_area,dropoff_community_area,fare,tolls,extras,trip_total',
        limit=10000,
    ).set_display_name('Training data').output

    testing_data = chicago_taxi_dataset_op(
        where='trip_start_timestamp >= "{}" AND trip_start_timestamp < "{}"'.format(str(testing_start_date), str(testing_end_date)),
        select='tips,trip_seconds,trip_miles,pickup_community_area,dropoff_community_area,fare,tolls,extras,trip_total',
        limit=10000,
    ).set_display_name('Testing data').output

    # Preparing the true values for the testing data
    true_values_table = pandas_transform_csv_op(
        table=testing_data,
        transform_code='''df = df[["tips"]]''',
    ).set_display_name('True values').output

    true_values = drop_header_op(true_values_table).output

    # Getting the active prod model
    prod_model_pointer_uri = str(model_dir_uri) + 'prod'
    get_prod_model_uri_task = download_from_gcs_op(
        gcs_path=prod_model_pointer_uri,
        default_data='',
    ).set_display_name('Get prod model')
    # Disabling cache reuse to always get new data
    get_prod_model_uri_task.execution_options.caching_strategy.max_cache_staleness = 'P0D'
    prod_model_uri = get_prod_model_uri_task.output

    # Training new model from scratch
    with kfp.dsl.Condition(prod_model_uri == ""):
        # Training
        model = xgboost_train_on_csv_op(
            training_data=training_data,
            label_column=0,
            objective='reg:squarederror',
            num_iterations=400,
        ).outputs['model']

        # Predicting
        predictions = xgboost_predict_on_csv_op(
            data=testing_data,
            model=model,
            label_column=0,
        ).output

        # Calculating the regression metrics
        metrics_task = calculate_regression_metrics_from_csv_op(
            true_values=true_values,
            predicted_values=predictions,
        )

        # Checking the metrics
        with kfp.dsl.Condition(metrics_task.outputs['mean_squared_error'] < 2.0):
            # Uploading the model
            model_uri = upload_to_gcs_unique_op(
                data=model,
                gcs_path_prefix=model_dir_uri,
            ).set_display_name('Upload model').output

            # Setting the model as prod
            upload_to_gcs_op(
                data=model_uri,
                gcs_path=prod_model_pointer_uri,
            ).set_display_name('Set prod model')

    # Training new model starting from the prod model
    with kfp.dsl.Condition(prod_model_uri != ""):
        # Downloading the model
        prod_model = download_from_gcs_op(prod_model_uri).output

        # Training
        model = xgboost_train_on_csv_op(
            training_data=training_data,
            starting_model=prod_model,
            label_column=0,
            objective='reg:squarederror',
            num_iterations=100,
        ).outputs['model']

        # Predicting
        predictions = xgboost_predict_on_csv_op(
            data=testing_data,
            model=model,
            label_column=0,
        ).output

        # Calculating the regression metrics
        metrics_task = calculate_regression_metrics_from_csv_op(
            true_values=true_values,
            predicted_values=predictions,
        )

        # Checking the metrics
        with kfp.dsl.Condition(metrics_task.outputs['mean_squared_error'] < 2.0):
            # Uploading the model
            model_uri = upload_to_gcs_unique_op(
                data=model,
                gcs_path_prefix=model_dir_uri,
            ).set_display_name('Upload model').output

            # Setting the model as prod
            upload_to_gcs_op(
                data=model_uri,
                gcs_path=prod_model_pointer_uri,
            ).set_display_name('Set prod model')


if __name__ == '__main__':
    # Running the first time. The trainer will train the model from scratch and set as prod after testing it
    pipelin_run = kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(
        continuous_training_pipeline,
        arguments=dict(
            model_dir_uri=model_dir_uri,
            training_start_date='2019-02-01',
            training_end_date='2019-03-01',
        ),
    )
    pipelin_run.wait_for_run_completion()

    # Running the second time. The trainer should warm-start the training from the prod model and set the new model as prod after testing it
    kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(
        continuous_training_pipeline,
        arguments=dict(
            model_dir_uri=model_dir_uri,
            training_start_date='2019-02-01',
            training_end_date='2019-03-01',
        ),
    )
