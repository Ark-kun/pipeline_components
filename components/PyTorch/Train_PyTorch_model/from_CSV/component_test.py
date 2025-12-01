import component

if __name__ == "__main__":
    component.train_pytorch_model_from_csv(
        model_path="../../Create_fully_connected_network/model.PyTorchScriptModule",
        training_data_path="training_data.csv",
        trained_model_path="trained_model.PyTorchScriptModule",
        label_column_name="tips",
        # Optional:
        number_of_epochs=100,
        learning_rate=0.2,
    )
