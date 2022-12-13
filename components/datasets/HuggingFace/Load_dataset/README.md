<!-- BEGIN_GENERATED_CONTENT -->
# Load dataset using huggingface

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/datasets/HuggingFace/Load_dataset/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/datasets/HuggingFace/Load_dataset/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dataset_name** **\***|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|dataset_dict|[HuggingFaceDatasetDict]||
|splits|[JsonArray]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
load_dataset_using_huggingface_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/datasets/HuggingFace/Load_dataset/component.yaml")
...
load_dataset_using_huggingface_task = load_dataset_using_huggingface_op(
    dataset_name=...,
)
```

## Other information

###### Tags

* input_type=[String]
* output_type=[HuggingFaceDatasetDict]
* output_type=[JsonArray]

[HuggingFaceDatasetDict]: https://github.com/Ark-kun/pipeline_components/tree/master/types/HuggingFaceDatasetDict
[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
