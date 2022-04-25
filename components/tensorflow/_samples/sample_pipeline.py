from kfp import components

chicago_taxi_dataset_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/8dda6ec74d859a0112907fab8bc987a177b9fa4b/components/datasets/Chicago_Taxi_Trips/component.yaml")
# See https://github.com/keras-team/keras/issues/16451
#create_fully_connected_tensorflow_network_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/8721c9c658b40d260ca90c4c8198cf12c2c88838/components/tensorflow/Create_fully_connected_network/component.yaml")
create_fully_connected_tensorflow_network_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/f3a9769d35a057c31a498e0667cae2e4a830c5b0/components/tensorflow/Create_fully_connected_network/component.yaml")

train_model_using_Keras_on_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/c504a4010348c50eaaf6d4337586ccc008f4dcef/components/tensorflow/Train_model_using_Keras/on_CSV/component.yaml")


def tensorflow_pipeline():
    feature_columns = ['trip_seconds', 'trip_miles', 'pickup_community_area', 'dropoff_community_area', 'fare', 'tolls', 'extras']  # Excluded 'trip_total'
    label_column = 'tips'
    network = create_fully_connected_tensorflow_network_op(
        layer_sizes=[len(feature_columns), 10, 1],
        activation_name='elu',
    ).output

    training_data = chicago_taxi_dataset_op(
        where='trip_start_timestamp >= "2019-01-01" AND trip_start_timestamp < "2019-02-01"',
        select=','.join([label_column] + feature_columns),
        limit=10000,
    ).output

    model1 = train_model_using_Keras_on_CSV_op(
        training_data=training_data,
        model=network,
        label_column_name=label_column,
        loss_function_name="mean_squared_error",
        metric_names=["mean_absolute_error"],
        number_of_epochs=10,
    ).outputs["trained_model"]

    model2 = train_model_using_Keras_on_CSV_op(
        training_data=training_data,
        model=model1,
        label_column_name=label_column,
        loss_function_name="mean_squared_error",
        metric_names=["mean_absolute_error"],
        number_of_epochs=10,
    ).outputs["trained_model"]


if __name__ == '__main__':
    import os
    import kfp
    kfp_endpoint = os.environ.get("KFP_ENDPOINT") #and os.environ.get("KFP_CREATE_RUN")
    if kfp_endpoint:
        import kfp
        kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(tensorflow_pipeline, arguments={})
