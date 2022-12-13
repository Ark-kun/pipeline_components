<!-- BEGIN_GENERATED_CONTENT -->
# Split rows into subsets

Description: Splits the data table according to the split fractions.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/dataset_manipulation/Split_rows_into_subsets/in_CSV/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/dataset_manipulation/Split_rows_into_subsets/in_CSV/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**table** **\***|[CSV]||Input data table.|
|**fraction_1** **\***|[Float]||The proportion of the lines to put into the 1st split. Range: [0, 1]|
|fraction_2|[Float]||The proportion of the lines to put into the 2nd split. Range: [0, 1]<br/>If fraction_2 is not specified, then fraction_2 = 1 - fraction_1.<br/>The remaining lines go to the 3rd split (if any).|
|random_seed|[Integer]|0|Controls the seed of the random processes.|

## Outputs

|Name|Type|Description|
|-|-|-|
|split_1|[CSV]|Subset of the data table.|
|split_2|[CSV]|Subset of the data table.|
|split_3|[CSV]|Subset of the data table.|
|split_1_count|[Integer]||
|split_2_count|[Integer]||
|split_3_count|[Integer]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
split_rows_into_subsets_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/dataset_manipulation/Split_rows_into_subsets/in_CSV/component.yaml")
...
split_rows_into_subsets_task = split_rows_into_subsets_op(
    table=...,
    fraction_1=...,
    # Optional:
    # fraction_2=...,
    # random_seed=0,
)
```

## Other information

###### Tags

* input_type=[CSV]
* input_type=[Float]
* input_type=[Integer]
* output_type=[CSV]
* output_type=[Integer]

[CSV]: https://github.com/Ark-kun/pipeline_components/tree/master/types/CSV
[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
<!-- END_GENERATED_CONTENT -->
