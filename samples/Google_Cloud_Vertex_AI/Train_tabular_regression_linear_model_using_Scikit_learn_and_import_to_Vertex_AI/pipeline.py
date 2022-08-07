# python3 -m pip install "kfp<2.0.0" "google-cloud-aiplatform>=1.16.0" --upgrade --quiet
from kfp import components

# %% Loading components
download_from_gcs_op = components.load_component_from_url("https://raw.githubusercontent.com/kubeflow/pipelines/c783705c0e566c611ef70160a01e3ed0865051bd/components/contrib/google-cloud/storage/download/component.yaml")
select_columns_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/0f0650b8446277b10f7ab48d220e413eef04ec69/components/pandas/Select_columns/in_CSV_format/component.yaml")
fill_all_missing_values_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/151411a5b719916b47505cd21c4541c1a5b62400/components/pandas/Fill_all_missing_values/in_CSV_format/component.yaml")
binarize_column_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/0c7b4ea8c7048cc5cd59c161bcbfa5b742738e99/components/pandas/Binarize_column/in_CSV_format/component.yaml")
train_linear_regression_model_using_scikit_learn_from_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/f807e02b54d4886c65a05f40848fd51c72407f40/components/ML_frameworks/Scikit_learn/Train_linear_regression_model/from_CSV/component.yaml")
upload_Scikit_learn_pickle_model_to_Google_Cloud_Vertex_AI_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/25dc317e649a19a53139a08ccbe496a248693fe4/components/google-cloud/Vertex_AI/Models/Upload_Scikit-learn_pickle_model/component.yaml")

# %% Pipeline definition
def train_tabular_regression_linear_model_using_Scikit_learn_pipeline():
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

    # Cleaning the NaN values.
    training_data = fill_all_missing_values_using_Pandas_on_CSV_data_op(
        table=training_data,
        replacement_value="0",
        #replacement_type_name="float",
    ).outputs["transformed_table"]

    model = train_linear_regression_model_using_scikit_learn_from_CSV_op(
        dataset=training_data,
        label_column_name=label_column,
    ).outputs["model"]

    vertex_model_name = upload_Scikit_learn_pickle_model_to_Google_Cloud_Vertex_AI_op(
        model=model,
    ).outputs["model_name"]

pipeline_func = train_tabular_regression_linear_model_using_Scikit_learn_pipeline

# %% Pipeline submission
if __name__ == '__main__':
    from google.cloud import aiplatform
    aiplatform.PipelineJob.from_pipeline_func(pipeline_func=pipeline_func).submit()
