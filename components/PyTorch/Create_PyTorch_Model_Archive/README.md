<!-- BEGIN_GENERATED_CONTENT -->
# Create PyTorch Model Archive

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/PyTorch/Create_PyTorch_Model_Archive/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/PyTorch/Create_PyTorch_Model_Archive/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Model** **\***|[PyTorchScriptModule]|||
|**Model name** **\***|[String]|model||
|**Model version** **\***|[String]|1.0||
|**Handler** **\***|[PythonCode]||See https://github.com/pytorch/serve/blob/master/docs/custom_service.md|

## Outputs

|Name|Type|Description|
|-|-|-|
|Model archive|[PyTorchModelArchive]||

## Implementation

#### Container

Container image: [pytorch/torchserve:0.5.2-cpu](https://hub.docker.com/r/pytorch/torchserve)

## Usage

```python
create_PyTorch_Model_Archive_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/PyTorch/Create_PyTorch_Model_Archive/component.yaml")
...
create_PyTorch_Model_Archive_task = create_PyTorch_Model_Archive_op(
    model=...,
    model_name=...,
    model_version=...,
    handler=...,
)
```

## Other information

###### Tags

* input_type=[PyTorchScriptModule]
* input_type=[PythonCode]
* input_type=[String]
* output_type=[PyTorchModelArchive]

[PyTorchModelArchive]: https://github.com/Ark-kun/pipeline_components/tree/master/types/PyTorchModelArchive
[PyTorchScriptModule]: https://github.com/Ark-kun/pipeline_components/tree/master/types/PyTorchScriptModule
[PythonCode]: https://github.com/Ark-kun/pipeline_components/tree/master/types/PythonCode
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
