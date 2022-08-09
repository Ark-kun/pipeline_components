from kfp import components


chicago_taxi_dataset_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/datasets/Chicago_Taxi_Trips/component.yaml')
pandas_transform_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml')
download_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/web/Download/component.yaml')

create_fully_connected_pytorch_network_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/9a6218944f3d36529812d23e959690dd2b061102/components/PyTorch/Create_fully_connected_network/component.yaml')
train_pytorch_model_from_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/PyTorch/Train_PyTorch_model/from_CSV/component.yaml')
convert_to_onnx_from_pytorch_script_module_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/PyTorch/Convert_to_OnnxModel_from_PyTorchScriptModule/component.yaml')
create_pytorch_model_archive_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/PyTorch/Create_PyTorch_Model_Archive/component.yaml')
create_pytorch_model_archive_with_base_handler_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/46d51383e6554b7f3ab4fd8cf614d8c2b422fb22/components/PyTorch/Create_PyTorch_Model_Archive/with_base_handler/component.yaml')


def pytorch_pipeline():
    feature_columns = ['trip_seconds', 'trip_miles', 'pickup_community_area', 'dropoff_community_area', 'fare', 'tolls', 'extras']  # Excluded 'trip_total'
    label_column = 'tips'
    network = create_fully_connected_pytorch_network_op(
        input_size=len(feature_columns),
        # Optional:
        hidden_layer_sizes=[100, 10],
        activation_name="elu",
        # output_activation_name=None,
        # output_size=1,
    ).outputs["model"]

    training_data = chicago_taxi_dataset_op(
        where='trip_start_timestamp >= "2019-01-01" AND trip_start_timestamp < "2019-02-01"',
        select=','.join([label_column] + feature_columns),
        limit=10000,
    ).output

    training_data = pandas_transform_csv_op(
        table=training_data,
        transform_code='''df = df.fillna({'tolls': 0.0, 'extras': 0.0}); df = df.dropna(axis='index')''',
    ).output

    trained_model = train_pytorch_model_from_csv_op(
        model=network,
        training_data=training_data,
        label_column_name=label_column,
        loss_function_name='mse_loss',
        # Optional:
        batch_size=32,
        number_of_epochs=2,
        random_seed=0,
        learning_rate=0.1,
        optimizer_name='Adadelta',
        optimizer_parameters={},
    ).outputs['trained_model']

    convert_to_onnx_from_pytorch_script_module_op(
        model=trained_model,
        list_of_input_shapes=[[len(feature_columns)]],
    )

    model_archive = create_pytorch_model_archive_with_base_handler_op(
        model=trained_model,
        # Optional:
        # model_name="model",
        # model_version="1.0",
    )

    # TODO: Use a real working regression handler here. See https://github.com/pytorch/serve/issues/987
    serving_handler = download_op('https://raw.githubusercontent.com/pytorch/serve/5c03e711a401387a1d42fc01072fcc38b4995b66/ts/torch_handler/base_handler.py').output

    model_archive2 = create_pytorch_model_archive_op(
        model=trained_model,
        handler=serving_handler,
        # model_name="model",  # Optional
        # model_version="1.0",  # Optional
    ).output

if __name__ == '__main__':
    import kfp
    kfp_endpoint=None
    kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(
        pytorch_pipeline,
        arguments={},
    )
