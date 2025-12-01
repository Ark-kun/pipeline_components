import component

if __name__ == "__main__":
    component.predict_with_PyTorch_model_on_CSV_data(
        model_path="../../Train_PyTorch_model/from_CSV/trained_model.PyTorchScriptModule",
        data_path="../../Train_PyTorch_model/from_CSV/training_data.csv",
        predictions_path="predictions.csv",
        label_column_name="tips",
        # Optional:
        prediction_column_name="prediction",
    )
