import component

if __name__ == "__main__":
    component.create_fully_connected_pytorch_network(
        model_path="model.PyTorchScriptModule",
        input_size=8,
        hidden_layer_sizes=[10],
        output_size=1,
    )
