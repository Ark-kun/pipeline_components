# cross_validation_pipeline compact
import kfp
from kfp import components


chicago_taxi_dataset_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/datasets/Chicago_Taxi_Trips/component.yaml')
xgboost_train_and_cv_regression_on_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train_and_cross-validate_regression/from_CSV/component.yaml')


def cross_validation_pipeline(
    label_column: int = 0,
    objective: str = 'reg:squarederror',
    num_iterations: int = 200,
):
    data = chicago_taxi_dataset_op(
        where='trip_start_timestamp >= "{}" AND trip_start_timestamp < "{}"'.format('2019-01-01', '2019-02-01'),
        select='tips,trip_seconds,trip_miles,pickup_community_area,dropoff_community_area,fare,tolls,extras,trip_total',
        limit=10000,
    ).output

    xgboost_train_and_cv_regression_on_csv_op(
        data=data,
        label_column=label_column,
        objective=objective,
        num_iterations=num_iterations,
    )


if __name__ == '__main__':
    kfp_endpoint=None
    kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(
        cross_validation_pipeline,
        arguments={},
    )
