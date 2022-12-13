<!-- BEGIN_GENERATED_CONTENT -->
# Create Vowpal Wabbit dataset from CSV

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/ML_frameworks/Vowpal_Wabbit/Create_dataset/from_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Vowpal_Wabbit/Create_dataset/from_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dataset** **\***|[CSV]|||
|label_column_name|[String]|||
|label_type|[String]|simple_label||

## Outputs

|Name|Type|Description|
|-|-|-|
|converted_dataset|[VowpalWabbitDataset]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
create_Vowpal_Wabbit_dataset_from_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Vowpal_Wabbit/Create_dataset/from_CSV/component.yaml")
...
create_Vowpal_Wabbit_dataset_from_CSV_task = create_Vowpal_Wabbit_dataset_from_CSV_op(
    dataset=...,
    # Optional:
    # label_column_name=...,
    # label_type="simple_label",
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[String]
* output_type=[VowpalWabbitDataset]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[VowpalWabbitDataset]: https://github.com/Ark-kun/pipeline_components/tree/master/types/VowpalWabbitDataset
<!-- END_GENERATED_CONTENT -->
