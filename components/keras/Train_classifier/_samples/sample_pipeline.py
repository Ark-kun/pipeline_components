import keras
import kfp
from kfp import components


chicago_taxi_dataset_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/datasets/Chicago_Taxi_Trips/component.yaml')
pandas_transform_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml')
keras_train_classifier_from_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/keras/Train_classifier/from_CSV/component.yaml')
keras_convert_hdf5_model_to_tf_saved_model_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/_converters/KerasModelHdf5/to_TensorflowSavedModel/component.yaml')


number_of_classes = 2

# Creating the network
dense_network_with_sigmoid = keras.Sequential(layers=[
    keras.layers.Dense(10, activation=keras.activations.sigmoid),
    keras.layers.Dense(number_of_classes, activation=keras.activations.sigmoid),
])


def keras_classifier_pipeline():
    training_data_in_csv = chicago_taxi_dataset_op(
        where='trip_start_timestamp >= "2019-01-01" AND trip_start_timestamp < "2019-02-01"',
        select='tips,trip_seconds,trip_miles,pickup_community_area,dropoff_community_area,fare,tolls,extras,trip_total',
        limit=1000,
    ).output

    training_data_for_classification_in_csv = pandas_transform_csv_op(
        table=training_data_in_csv,
        transform_code='''df.insert(0, "was_tipped", df["tips"] > 0); del df["tips"]; df = df.fillna(0)''',
    ).output

    features_in_csv = pandas_transform_csv_op(
        table=training_data_for_classification_in_csv,
        transform_code='''df = df.drop(columns=["was_tipped"])''',
    ).output

    labels_in_csv = pandas_transform_csv_op(
        table=training_data_for_classification_in_csv,
        transform_code='''df = df["was_tipped"] * 1''',
    ).output

    keras_model_in_hdf5 = keras_train_classifier_from_csv_op(
        training_features=features_in_csv,
        training_labels=labels_in_csv,
        network_json=dense_network_with_sigmoid.to_json(),
        learning_rate=0.1,
        num_epochs=100,
    ).outputs['model']

    keras_model_in_tf_format = keras_convert_hdf5_model_to_tf_saved_model_op(
        model=keras_model_in_hdf5,
    ).output

if __name__ == '__main__':
    kfp_endpoint = None
    kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(keras_classifier_pipeline, arguments={})
