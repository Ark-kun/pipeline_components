from kfp.components import create_component_from_func, OutputPath

def create_fully_connected_pytorch_network(
    input_size: int,
    model_path: OutputPath('PyTorchScriptModule'),
    hidden_layer_sizes: list = [],
    output_size: int = 1,
    activation_name: str = 'relu',
    output_activation_name: str = None,
    random_seed: int = 0,
):
    """Creates untrained fully-connected network in PyTorch ScriptModule format.

    Args:
        input_size: Size of the input vector.
        model_path: Untrained model in PyTorch Script Module format.
        hidden_layer_sizes: Sizes of the hidden layers.
        output_size: Size of the output vector.
        activation_name: Name of the activation function used between layers.
        output_activation_name: Name of the activation function used after output layers.
        random_seed: Controls the seed of the random processes.
    """
    import torch
    torch.manual_seed(random_seed)

    activation = getattr(torch, activation_name, None) or getattr(torch.nn.functional, activation_name, None)
    if not activation:
        raise ValueError(f'Activation "{activation_name}" was not found.')

    class ActivationLayer(torch.nn.Module):
        def forward(self, input):
            return activation(input)

    layers = []
    prev_layer_size = input_size
    for layer_size in hidden_layer_sizes:
        layer = torch.nn.Linear(prev_layer_size, layer_size)
        prev_layer_size = layer_size
        layers.append(layer)
        layers.append(ActivationLayer())

    # Adding the output layer
    layers.append(torch.nn.Linear(prev_layer_size, output_size))

    # Adding the optional activation after the output layer
    if output_activation_name:
        output_activation = getattr(torch, output_activation_name, None) or getattr(torch.nn.functional, output_activation_name, None)
        class OutputActivationLayer(torch.nn.Module):
            def forward(self, input):
                return output_activation(input)
        layers.append(OutputActivationLayer())

    network = torch.nn.Sequential(*layers)
    script_module = torch.jit.script(network)
    print(script_module)
    script_module.save(model_path)


if __name__ == '__main__':
    create_fully_connected_pytorch_network_op = create_component_from_func(
        create_fully_connected_pytorch_network,
        output_component_file='component.yaml',
        base_image='pytorch/pytorch:1.7.1-cuda11.0-cudnn8-runtime',
        packages_to_install=[],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/PyTorch/Create_fully_connected_network/component.yaml",
        },
    )
