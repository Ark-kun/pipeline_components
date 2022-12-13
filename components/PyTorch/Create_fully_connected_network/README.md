<!-- BEGIN_GENERATED_CONTENT -->
# Create fully connected pytorch network

Description: Creates untrained fully-connected network in PyTorch ScriptModule format.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/PyTorch/Create_fully_connected_network/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/PyTorch/Create_fully_connected_network/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**input_size** **\***|[Integer]||Size of the input vector.|
|hidden_layer_sizes|[JsonArray]|[]|Sizes of the hidden layers.|
|output_size|[Integer]|1|Size of the output vector.|
|activation_name|[String]|relu|Name of the activation function used between layers.|
|output_activation_name|[String]||Name of the activation function used after output layers.|
|random_seed|[Integer]|0|Controls the seed of the random processes.|

## Outputs

|Name|Type|Description|
|-|-|-|
|model|[PyTorchScriptModule]|Untrained model in PyTorch Script Module format.|

## Implementation

#### Container

Container image: [pytorch/pytorch:1.7.1-cuda11.0-cudnn8-runtime](https://hub.docker.com/r/pytorch/pytorch)

## Usage

```python
create_fully_connected_pytorch_network_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/PyTorch/Create_fully_connected_network/component.yaml")
...
create_fully_connected_pytorch_network_task = create_fully_connected_pytorch_network_op(
    input_size=...,
    # Optional:
    # hidden_layer_sizes="[]",
    # output_size=1,
    # activation_name="relu",
    # output_activation_name=...,
    # random_seed=0,
)
```

## Other information

###### Tags

* input_type=[Integer]
* input_type=[JsonArray]
* input_type=[String]
* output_type=[PyTorchScriptModule]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[PyTorchScriptModule]: https://github.com/Ark-kun/pipeline_components/tree/master/types/PyTorchScriptModule
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
