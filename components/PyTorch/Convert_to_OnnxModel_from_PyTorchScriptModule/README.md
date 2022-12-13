<!-- BEGIN_GENERATED_CONTENT -->
# Convert to OnnxModel from PyTorchScriptModule

Description: Creates fully-connected network in PyTorch ScriptModule format

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/PyTorch/Convert_to_OnnxModel_from_PyTorchScriptModule/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/PyTorch/Convert_to_OnnxModel_from_PyTorchScriptModule/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**model** **\***|[PyTorchScriptModule]|||
|**list_of_input_shapes** **\***|[JsonArray]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|converted_model|[OnnxModel]||

## Implementation

#### Container

Container image: [pytorch/pytorch:1.7.1-cuda11.0-cudnn8-runtime](https://hub.docker.com/r/pytorch/pytorch)

## Usage

```python
convert_to_OnnxModel_from_PyTorchScriptModule_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/PyTorch/Convert_to_OnnxModel_from_PyTorchScriptModule/component.yaml")
...
convert_to_OnnxModel_from_PyTorchScriptModule_task = convert_to_OnnxModel_from_PyTorchScriptModule_op(
    model=...,
    list_of_input_shapes=...,
)
```

## Other information

###### Tags

* input_type=[JsonArray]
* input_type=[PyTorchScriptModule]
* output_type=[OnnxModel]

[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[OnnxModel]: https://github.com/Ark-kun/pipeline_components/tree/master/types/OnnxModel
[PyTorchScriptModule]: https://github.com/Ark-kun/pipeline_components/tree/master/types/PyTorchScriptModule
<!-- END_GENERATED_CONTENT -->
