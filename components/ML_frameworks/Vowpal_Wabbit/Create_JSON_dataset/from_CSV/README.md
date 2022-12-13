<!-- BEGIN_GENERATED_CONTENT -->
# Create Vowpal Wabbit JSON dataset from CSV

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/ML_frameworks/Vowpal_Wabbit/Create_JSON_dataset/from_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Vowpal_Wabbit/Create_JSON_dataset/from_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**dataset** **\***|[CSV]|||
|label_column_name|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|converted_dataset|[VowpalWabbitJsonDataset]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
create_Vowpal_Wabbit_JSON_dataset_from_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Vowpal_Wabbit/Create_JSON_dataset/from_CSV/component.yaml")
...
create_Vowpal_Wabbit_JSON_dataset_from_CSV_task = create_Vowpal_Wabbit_JSON_dataset_from_CSV_op(
    dataset=...,
    # Optional:
    # label_column_name=...,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[String]
* output_type=[VowpalWabbitJsonDataset]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[VowpalWabbitJsonDataset]: https://github.com/Ark-kun/pipeline_components/tree/master/types/VowpalWabbitJsonDataset
<!-- END_GENERATED_CONTENT -->
