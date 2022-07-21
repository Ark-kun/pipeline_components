# pip install "kfp<2.0.0" "google-cloud-aiplatform>=1.15.1" --upgrade --quiet
from kfp import components

# %% Loading components
download_from_gcs_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/google-cloud/storage/download/component.yaml")
select_columns_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/0f0650b8446277b10f7ab48d220e413eef04ec69/components/pandas/Select_columns/in_CSV_format/component.yaml")
binarize_column_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/0c7b4ea8c7048cc5cd59c161bcbfa5b742738e99/components/pandas/Binarize_column/in_CSV_format/component.yaml")
xgboost_train_on_csv_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml")
xgboost_predict_on_csv_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml")

# %% Pipeline definition
def train_tabular_regression_model_using_XGBoost_pipeline():
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

    model = xgboost_train_on_csv_op(
        training_data=training_data,
        label_column=0,
        # Optional:
        #starting_model=None,
        #num_iterations=10,
        #booster_params={},
        #objective="reg:squarederror",
        #booster="gbtree",
        #learning_rate=0.3,
        #min_split_loss=0,
        #max_depth=6,
    ).outputs["model"]

    # Predicting on the training data
    predictions = xgboost_predict_on_csv_op(
        data=training_data,
        model=model,
        # label_column needs to be set when doing prediction on a dataset that has labels
        label_column=0,
    ).outputs["predictions"]

pipeline_func = train_tabular_regression_model_using_XGBoost_pipeline

# %% Pipeline submission
if __name__ == "__main__":
    import os
    import kfp

    kfp_endpoint = os.environ.get("KFP_ENDPOINT")
    kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(
        pipeline_func,
        arguments={},
    )