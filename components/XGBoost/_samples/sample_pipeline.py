import kfp
from kfp import components


chicago_taxi_dataset_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/datasets/Chicago_Taxi_Trips/component.yaml')
convert_csv_to_apache_parquet_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/_converters/ApacheParquet/from_CSV/component.yaml')
xgboost_train_on_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml')
xgboost_predict_on_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml')
xgboost_train_on_parquet_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/from_ApacheParquet/component.yaml')
xgboost_predict_on_parquet_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/from_ApacheParquet/component.yaml')


def xgboost_pipeline():
    training_data_csv = chicago_taxi_dataset_op(
        where='trip_start_timestamp >= "2019-01-01" AND trip_start_timestamp < "2019-02-01"',
        select='tips,trip_seconds,trip_miles,pickup_community_area,dropoff_community_area,fare,tolls,extras,trip_total',
        limit=10000,
    ).output

    # Training and prediction on dataset in CSV format
    model_trained_on_csv = xgboost_train_on_csv_op(
        training_data=training_data_csv,
        label_column=0,
        objective='reg:squarederror',
        num_iterations=200,
    ).outputs['model']

    xgboost_predict_on_csv_op(
        data=training_data_csv,
        model=model_trained_on_csv,
        label_column=0,
    )

    # Training and prediction on dataset in Apache Parquet format
    training_data_parquet = convert_csv_to_apache_parquet_op(
        training_data_csv
    ).output

    model_trained_on_parquet = xgboost_train_on_parquet_op(
        training_data=training_data_parquet,
        label_column_name='tips',
        objective='reg:squarederror',
        num_iterations=200,
    ).outputs['model']

    xgboost_predict_on_parquet_op(
        data=training_data_parquet,
        model=model_trained_on_parquet,
        label_column_name='tips',
    )

    # Checking cross-format predictions
    xgboost_predict_on_parquet_op(
        data=training_data_parquet,
        model=model_trained_on_csv,
        label_column_name='tips',
    )

    xgboost_predict_on_csv_op(
        data=training_data_csv,
        model=model_trained_on_parquet,
        label_column=0,
    )


if __name__ == '__main__':
    kfp_endpoint=None
    kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(xgboost_pipeline, arguments={})
