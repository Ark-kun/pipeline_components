#!/usr/bin/env python3

# This sample demonstrates continuous training using a train-eval-check recursive loop.
# The main pipeline trains the initial model and then gradually trains the model
# some more until the model evaluation metrics are good enough.

import kfp
from kfp import components


chicago_taxi_dataset_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/datasets/Chicago_Taxi_Trips/component.yaml')
xgboost_train_on_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml')
xgboost_predict_on_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml')

pandas_transform_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml')
drop_header_op = kfp.components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml')
calculate_regression_metrics_from_csv_op = kfp.components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml')


# This recursive sub-pipeline trains a model, evaluates it, calculates the metrics and checks them.
# If the model error is too high, then more training is performed until the model is good.
@kfp.dsl.graph_component
def train_until_low_error(starting_model, training_data, true_values):
    # Training
    model = xgboost_train_on_csv_op(
        training_data=training_data,
        starting_model=starting_model,
        label_column=0,
        objective='reg:squarederror',
        num_iterations=50,
    ).outputs['model']

    # Predicting
    predictions = xgboost_predict_on_csv_op(
        data=training_data,
        model=model,
        label_column=0,
    ).output

    # Calculating the regression metrics
    metrics_task = calculate_regression_metrics_from_csv_op(
        true_values=true_values,
        predicted_values=predictions,
    )

    # Checking the metrics
    with kfp.dsl.Condition(metrics_task.outputs['mean_squared_error'] > 0.01):
        # Training some more
        train_until_low_error(
            starting_model=model,
            training_data=training_data,
            true_values=true_values,
        )


# The main pipleine trains the initial model and then gradually trains the model some more until the model evaluation metrics are good enough.
def train_until_good_pipeline():
    # Preparing the training data
    training_data = chicago_taxi_dataset_op(
        where='trip_start_timestamp >= "2019-01-01" AND trip_start_timestamp < "2019-02-01"',
        select='tips,trip_seconds,trip_miles,pickup_community_area,dropoff_community_area,fare,tolls,extras,trip_total',
        limit=10000,
    ).output

    # Preparing the true values
    true_values_table = pandas_transform_csv_op(
        table=training_data,
        transform_code='df = df[["tips"]]',
    ).output

    true_values = drop_header_op(true_values_table).output

    # Initial model training
    first_model = xgboost_train_on_csv_op(
        training_data=training_data,
        label_column=0,
        objective='reg:squarederror',
        num_iterations=100,
    ).outputs['model']

    # Recursively training until the error becomes low
    train_until_low_error(
        starting_model=first_model,
        training_data=training_data,
        true_values=true_values,
    )


if __name__ == '__main__':
    kfp_endpoint=None
    kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(train_until_good_pipeline, arguments={})
