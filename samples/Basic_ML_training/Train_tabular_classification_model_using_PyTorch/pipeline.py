# python3 -m pip install "kfp<2.0.0" --upgrade --quiet
from kfp import components

# %% Loading components
download_from_gcs_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/google-cloud/storage/download/component.yaml")
select_columns_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/8c78aae096806cff3bc331a40566f42f5c3e9d4b/components/pandas/Select_columns/in_CSV_format/component.yaml")
fill_all_missing_values_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/23405971f5f16a41b16c343129b893c52e4d1d48/components/pandas/Fill_all_missing_values/in_CSV_format/component.yaml")
binarize_column_using_Pandas_on_CSV_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/1e2558325f4c708aca75827c8acc13d230ee7e9f/components/pandas/Binarize_column/in_CSV_format/component.yaml")
create_fully_connected_pytorch_network_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/1a2ef3eeb77bc278f33cad0dd29008ea2431e191/components/PyTorch/Create_fully_connected_network/component.yaml")
train_pytorch_model_from_csv_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/PyTorch/Train_PyTorch_model/from_CSV/component.yaml")
create_pytorch_model_archive_with_base_handler_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/46d51383e6554b7f3ab4fd8cf614d8c2b422fb22/components/PyTorch/Create_PyTorch_Model_Archive/with_base_handler/component.yaml")
convert_to_onnx_from_pytorch_script_module_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/PyTorch/Convert_to_OnnxModel_from_PyTorchScriptModule/component.yaml")

# %% Pipeline definition
def train_tabular_classification_model_using_PyTorch_pipeline():
    dataset_gcs_uri = "gs://ml-pipeline-dataset/Chicago_taxi_trips/chicago_taxi_trips_2019-01-01_-_2019-02-01_limit=10000.csv"
    feature_columns = ["trip_seconds", "trip_miles", "pickup_community_area", "dropoff_community_area", "fare", "tolls", "extras"]  # Excluded "trip_total"
    label_column = "tips"

    classification_label_column = "class"
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

    classification_training_data = binarize_column_using_Pandas_on_CSV_data_op(
        table=training_data,
        column_name=label_column,
        predicate=" > 0",
        new_column_name=classification_label_column,
    ).outputs["transformed_table"]

    network = create_fully_connected_pytorch_network_op(
        input_size=len(feature_columns),
        # Optional:
        hidden_layer_sizes=[10],
        activation_name="elu",
        output_activation_name="sigmoid",
        # output_size=1,
    ).outputs["model"]

    model = train_pytorch_model_from_csv_op(
        model=network,
        training_data=classification_training_data,
        label_column_name=classification_label_column,
        loss_function_name="binary_cross_entropy",
        # Optional:
        #number_of_epochs=1,
        #learning_rate=0.1,
        #optimizer_name="Adadelta",
        #optimizer_parameters={},
        #batch_size=32,
        #batch_log_interval=100,
        #random_seed=0,
    ).outputs["trained_model"]

    model_archive = create_pytorch_model_archive_with_base_handler_op(
        model=model,
        # Optional:
        # model_name="model",
        # model_version="1.0",
    ).outputs["Model archive"]

    onnx_model = convert_to_onnx_from_pytorch_script_module_op(
        model=model,
        list_of_input_shapes=[[len(feature_columns)]],
    ).outputs["converted_model"]


pipeline_func = train_tabular_classification_model_using_PyTorch_pipeline

# %% Pipeline submission
if __name__ == "__main__":
    import kfp
    # Set the KF_PIPELINES_ENDPOINT environment variable to the KFP endpoint URL:
    # import os; os.environ["KF_PIPELINES_ENDPOINT"] = "https://XXXXXXXXXXXXXXXX-dot-us-central2.pipelines.googleusercontent.com"
    kfp.Client().create_run_from_pipeline_func(
        pipeline_func,
        arguments={},
    )
