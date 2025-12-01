import component


if __name__ == "__main__":
    import pandas
    pandas.read_csv("training_data.csv").to_parquet("training_data.parquet")
    component.train_pytorch_model_from_ApacheParquet(
        model_path="../../Create_fully_connected_network/model.PyTorchScriptModule",
        training_data_path="training_data.parquet",
        trained_model_path="trained_model.PyTorchScriptModule",
        label_column_name="tips",
        # Optional:
        number_of_epochs=10,
        learning_rate=0.1,
    )
