<!-- BEGIN_GENERATED_CONTENT -->
# Split table into folds

Description: Splits the data table into the specified number of folds.

    The data is split into the specified number of folds k (default: 5).
    Each testing subsample has 1/k fraction of samples. The testing subsamples do not overlap.
    Each training subsample has (k-1)/k fraction of samples.
    The train_i subsample is produced by excluding test_i subsample form all samples.

    Inputs:
        table: The data to split by rows
        number_of_folds: Number of folds to split data into
        random_seed: Random seed for reproducible splitting

    Outputs:
        train_i: The i-th training subsample
        test_i: The i-th testing subsample

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/dataset_manipulation/split_data_into_folds/in_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/dataset_manipulation/split_data_into_folds/in_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**table** **\***|[CSV]|||
|number_of_folds|[Integer]|5||
|random_seed|[Integer]|0||

## Outputs

|Name|Type|Description|
|-|-|-|
|train_1|[CSV]||
|train_2|[CSV]||
|train_3|[CSV]||
|train_4|[CSV]||
|train_5|[CSV]||
|test_1|[CSV]||
|test_2|[CSV]||
|test_3|[CSV]||
|test_4|[CSV]||
|test_5|[CSV]||

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
split_table_into_folds_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/dataset_manipulation/split_data_into_folds/in_CSV/component.yaml")
...
split_table_into_folds_task = split_table_into_folds_op(
    table=...,
    # Optional:
    # number_of_folds=5,
    # random_seed=0,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[Integer]
* output_type=[CSV]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
<!-- END_GENERATED_CONTENT -->
