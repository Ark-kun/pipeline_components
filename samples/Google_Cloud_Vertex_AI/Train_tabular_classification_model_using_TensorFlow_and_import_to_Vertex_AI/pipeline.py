# pip install "kfp<2.0.0" "google-cloud-aiplatform>=1.15.1" --upgrade --quiet
from kfp import components

# %% Loading components
download_from_gcs_op = components.load_component_from_url("https://raw.githubusercontent.com/kubeflow/pipelines/c783705c0e566c611ef70160a01e3ed0865051bd/components/contrib/google-cloud/storage/download/component.yaml")
select_columns_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/0f0650b8446277b10f7ab48d220e413eef04ec69/components/pandas/Select_columns/in_CSV_format/component.yaml")
binarize_column_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/0c7b4ea8c7048cc5cd59c161bcbfa5b742738e99/components/pandas/Binarize_column/in_CSV_format/component.yaml")
create_fully_connected_tensorflow_network_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/6885e20e56de1e583c6101c42142be79ea7df363/components/tensorflow/Create_fully_connected_network/component.yaml")
train_model_using_Keras_on_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/c504a4010348c50eaaf6d4337586ccc008f4dcef/components/tensorflow/Train_model_using_Keras/on_CSV/component.yaml")
upload_Tensorflow_model_to_Google_Cloud_Vertex_AI_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/719783ef44c04348ea23e247a93021d91cfe602d/components/google-cloud/Vertex_AI/Models/Upload_Tensorflow_model/component.yaml")

# %% Pipeline definition
def train_tabular_classification_model_using_TensorFlow_pipeline():
    dataset_gcs_uri = "gs://ml-pipeline-dataset/Chicago_taxi_trips/chicago_taxi_trips_2019-01-01_-_2019-02-01_limit=10000.csv"
    feature_columns = ["trip_seconds", "trip_miles", "pickup_community_area", "dropoff_community_area", "fare", "tolls", "extras"]  # Excluded "trip_total"
    label_column = "tips"
    all_columns = [label_column] + feature_columns

    training_data = download_from_gcs_op(
        gcs_path=dataset_gcs_uri
    ).outputs["Data"]

    training_data = select_columns_using_Pandas_on_CSV_data_op(
        table=training_data,
        column_names=all_columns,
    ).outputs["transformed_table"]

    classification_training_data = binarize_column_using_Pandas_on_CSV_data_op(
        table=training_data,
        column_name=label_column,
        predicate=" > 0",
        new_column_name="class",
    ).outputs["transformed_table"]

    network = create_fully_connected_tensorflow_network_op(
        layer_sizes=[len(feature_columns), 10, 1],
        activation_name="elu",
        output_activation_name="sigmoid",
    ).outputs["model"]

    model = train_model_using_Keras_on_CSV_op(
        training_data=classification_training_data,
        model=network,
        label_column_name="class",
        # Optional:
        loss_function_name="binary_crossentropy",
        number_of_epochs=10,
        #learning_rate=0.1,
        #optimizer_name="Adadelta",
        #optimizer_parameters={},
        #batch_size=32,
        #metric_names=["mean_absolute_error"],
        #random_seed=0,
    ).outputs["trained_model"]

    vertex_model = upload_Tensorflow_model_to_Google_Cloud_Vertex_AI_op(
        model=model,
    ).outputs["model_name"]

pipeline_func = train_tabular_classification_model_using_TensorFlow_pipeline

# %% Pipeline submission
if __name__ == '__main__':
    from google.cloud import aiplatform
    aiplatform.PipelineJob.from_pipeline_func(pipeline_func=pipeline_func).submit()
