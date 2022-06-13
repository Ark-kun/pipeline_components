from kfp import components

# %% Loading components
download_from_gcs_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/google-cloud/storage/download/component.yaml")
select_columns_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/0f0650b8446277b10f7ab48d220e413eef04ec69/components/pandas/Select_columns/in_CSV_format/component.yaml")
create_fully_connected_tensorflow_network_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/f3a9769d35a057c31a498e0667cae2e4a830c5b0/components/tensorflow/Create_fully_connected_network/component.yaml")
train_model_using_Keras_on_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/c504a4010348c50eaaf6d4337586ccc008f4dcef/components/tensorflow/Train_model_using_Keras/on_CSV/component.yaml")

# %% Pipeline definition
def train_tabular_regression_model_using_Tensorflow_pipeline():
    dataset_gcs_uri = "gs://ml-pipeline-dataset/Chicago_taxi_trips/chicago_taxi_trips_2019-01-01_-_2019-02-01_limit=10000.csv"
    feature_columns = ["trip_seconds", "trip_miles", "pickup_community_area", "dropoff_community_area", "fare", "tolls", "extras"]  # Excluded "trip_total"
    label_column = "tips"
    all_columns = feature_columns + [label_column]

    training_data = download_from_gcs_op(
        gcs_path=dataset_gcs_uri
    ).outputs["Data"]

    training_data = select_columns_using_Pandas_on_CSV_data_op(
        table=training_data,
        column_names=all_columns,
    ).outputs["transformed_table"]

    network = create_fully_connected_tensorflow_network_op(
        layer_sizes=[len(feature_columns), 10, 1],
        activation_name="elu",
    ).output

    model = train_model_using_Keras_on_CSV_op(
        training_data=training_data,
        model=network,
        label_column_name=label_column,
        # Optional:
        #loss_function_name="mean_squared_error",
        number_of_epochs=10,
        #learning_rate=0.1,
        #optimizer_name="Adadelta",
        #optimizer_parameters={},
        #batch_size=32,
        metric_names=["mean_absolute_error"],
        #random_seed=0,
    ).outputs["trained_model"]


pipeline_func=train_tabular_regression_model_using_Tensorflow_pipeline

# %% Pipeline submission
if __name__ == '__main__':
    import os
    import kfp

    kfp_endpoint = os.environ.get("KFP_ENDPOINT")
    kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(
        pipeline_func,
        arguments={},
    )