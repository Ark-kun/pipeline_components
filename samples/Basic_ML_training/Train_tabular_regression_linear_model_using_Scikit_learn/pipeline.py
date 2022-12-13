# python3 -m pip install "kfp<2.0.0" --upgrade --quiet
from kfp import components

# %% Loading components
download_from_gcs_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/google-cloud/storage/download/component.yaml")
select_columns_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/8c78aae096806cff3bc331a40566f42f5c3e9d4b/components/pandas/Select_columns/in_CSV_format/component.yaml")
fill_all_missing_values_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/23405971f5f16a41b16c343129b893c52e4d1d48/components/pandas/Fill_all_missing_values/in_CSV_format/component.yaml")
train_linear_regression_model_using_scikit_learn_from_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/69a3fccb23196e6f7f731da62da6c8836c594728/components/ML_frameworks/Scikit_learn/Train_linear_regression_model/from_CSV/component.yaml")

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


pipeline_func = train_tabular_regression_linear_model_using_Scikit_learn_pipeline

# %% Pipeline submission
if __name__ == "__main__":
    import kfp
    # Set the KF_PIPELINES_ENDPOINT environment variable to the KFP endpoint URL:
    # import os; os.environ["KF_PIPELINES_ENDPOINT"] = "https://XXXXXXXXXXXXXXXX-dot-us-central2.pipelines.googleusercontent.com"
    kfp.Client().create_run_from_pipeline_func(
        pipeline_func,
        arguments={},
    )
