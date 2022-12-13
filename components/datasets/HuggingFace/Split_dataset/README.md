<!-- BEGIN_GENERATED_CONTENT -->
# Split dataset huggingface

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/datasets/HuggingFace/Split_dataset/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/datasets/HuggingFace/Split_dataset/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dataset_dict** **\***|[HuggingFaceDatasetDict]|||
|split_name|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|dataset_split|[HuggingFaceDataset]||
|dataset|[HuggingFaceArrowDataset]||
|dataset_info|[JsonObject]||
|dataset_state|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
split_dataset_huggingface_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/datasets/HuggingFace/Split_dataset/component.yaml")
...
split_dataset_huggingface_task = split_dataset_huggingface_op(
    dataset_dict=...,
    # Optional:
    # split_name=...,
)
```

## Other information

###### Tags

* input_type=[HuggingFaceDatasetDict]
* input_type=[String]
* output_type=[HuggingFaceArrowDataset]
* output_type=[HuggingFaceDataset]
* output_type=[JsonObject]

[HuggingFaceArrowDataset]: https://github.com/Ark-kun/pipeline_components/tree/master/types/HuggingFaceArrowDataset
[HuggingFaceDataset]: https://github.com/Ark-kun/pipeline_components/tree/master/types/HuggingFaceDataset
[HuggingFaceDatasetDict]: https://github.com/Ark-kun/pipeline_components/tree/master/types/HuggingFaceDatasetDict
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
