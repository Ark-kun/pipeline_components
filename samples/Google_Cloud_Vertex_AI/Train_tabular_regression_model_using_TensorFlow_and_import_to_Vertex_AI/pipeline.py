# pip install kfp google-cloud-aiplatform --upgrade --quiet
from kfp import components

# %% Loading components
download_from_gcs_op = components.load_component_from_url("https://raw.githubusercontent.com/kubeflow/pipelines/c783705c0e566c611ef70160a01e3ed0865051bd/components/contrib/google-cloud/storage/download/component.yaml")
select_columns_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/0f0650b8446277b10f7ab48d220e413eef04ec69/components/pandas/Select_columns/in_CSV_format/component.yaml")
create_fully_connected_tensorflow_network_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/f3a9769d35a057c31a498e0667cae2e4a830c5b0/components/tensorflow/Create_fully_connected_network/component.yaml")
train_model_using_Keras_on_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/c504a4010348c50eaaf6d4337586ccc008f4dcef/components/tensorflow/Train_model_using_Keras/on_CSV/component.yaml")
upload_Tensorflow_model_to_Google_Cloud_Vertex_AI_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/719783ef44c04348ea23e247a93021d91cfe602d/components/google-cloud/Vertex_AI/Models/Upload_Tensorflow_model/component.yaml")

# %% Pipeline definition
def train_tabular_regression_model_using_Tensorflow_pipeline():
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

    vertex_model_name = upload_Tensorflow_model_to_Google_Cloud_Vertex_AI_op(
        model=model,
    ).outputs["model_name"]

pipeline_func=train_tabular_regression_model_using_Tensorflow_pipeline

# %% Pipeline submission
if __name__ == '__main__':
    # pip install --upgrade --no-deps --force-reinstall "git+https://github.com/Ark-kun/python-aiplatform@feat--Added-the-PipelineJob.submit_from_pipeline_func-method#egg=google-cloud-aiplatform&subdirectory=."
    from google.cloud import aiplatform

    pipeline_job = aiplatform.PipelineJob.submit_from_pipeline_func(
        pipeline_func=pipeline_func,
        arguments={},
    )
