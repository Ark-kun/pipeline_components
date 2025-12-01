from cloud_pipelines.components import InputPath, OutputPath, create_component_from_func


def predict_with_PyTorch_model_on_CSV_data(
    data_path: InputPath("CSV"),
    model_path: InputPath("PyTorchScriptModule"),
    predictions_path: OutputPath("CSV"),
    label_column_name: str = None,
    prediction_column_name: str = "prediction",
    batch_size: int = 100,
):
    """Makes predictions using a trained PyTorch model.

    Args:
        data_path: Feature data in CSV format.
        model_path: Trained model in binary PyTorchScriptModule format.
        predictions_path: Model predictions.
        label_column_name: Optional. Name of the column containing the label data that is excluded during the prediction.
    """
    from pathlib import Path

    import numpy
    import pandas
    import torch

    model = torch.jit.load(model_path)
    # Switch the model to evaluation mode
    model.eval()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"{torch.cuda.is_available()=}")
    print(f"{device=}")
    model.to(device)

    df = pandas.read_csv(
        data_path,
    ).convert_dtypes()
    print("Evaluation data information:")
    df.info(verbose=True)

    if label_column_name is not None:
        features_df = df.drop(columns=[label_column_name])
    else:
        features_df = df

    # TODO: Batch processing
    features_numpy = features_df.to_numpy(dtype=numpy.float32)
    features_tensor = torch.tensor(features_numpy).to(device)
    print(f"{features_tensor.shape=}")
    predictions_tensor = model(features_tensor)
    predictions = predictions_tensor.cpu().detach().numpy()

    # Insert predictions column first
    df.insert(loc=0, column=prediction_column_name, value=predictions)

    Path(predictions_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(predictions_path, index=False)


if __name__ == "__main__":
    predict_with_PyTorch_model_on_CSV_data_op = create_component_from_func(
        predict_with_PyTorch_model_on_CSV_data,
        output_component_file="component.yaml",
        base_image="pytorch/pytorch:1.7.1-cuda11.0-cudnn8-runtime",
        packages_to_install=[
            "pandas==2.0.3",
            "numpy==1.24.4",
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/PyTorch/Predict/on_CSV/component.yaml",
            "python_dependencies_time": "2025-11-30",
        },
    )
