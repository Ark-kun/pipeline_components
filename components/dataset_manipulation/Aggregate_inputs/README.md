# Input Aggregator

Author: Morgan Wowk <morgan.wowk@gmail.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/dataset_manipulation/Aggregate_inputs/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/dataset_manipulation/Aggregate_inputs/component.yaml)

Aggregates multiple pipeline inputs into a single output. Supports JsonArray, JsonObject, and CSV aggregation modes. Pass values as `agg_N` inputs and set `output_type` to control the aggregation format.

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|output_type|[String]|JsonArray|Output format: `JsonArray` (array of values), `JsonObject` (keyed by input name), or `CSV` (union of CSV inputs with matching columns).|
|agg_1, agg_2, ...|[String]||Values to aggregate. Inputs are added dynamically at runtime — one per value to aggregate.|

## Outputs

|Name|Type|Description|
|-|-|-|
|Output|[String]|The aggregated result in the format specified by `output_type`.|

## Implementation

#### Container

Container image: [python:3.12-slim](https://hub.docker.com/_/python)

## Usage

```python
input_aggregator_op = components.load_component_from_url(
    "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/dataset_manipulation/Aggregate_inputs/component.yaml"
)
...
input_aggregator_task = input_aggregator_op(
    output_type="JsonArray",
    agg_1=...,
    agg_2=...,
)
```

### Output type examples

**`JsonArray`** — produces an ordered array of input values:
```json
["value1", "value2", "value3"]
```

**`JsonObject`** — produces an object keyed by input name (`agg_1`, `agg_2`, ...):
```json
{"agg_1": "value1", "agg_2": "value2", "agg_3": "value3"}
```

**`CSV`** — unions multiple CSV inputs with matching columns (header row from first input, subsequent headers are discarded):
```
col_a,col_b
row1a,row1b
row2a,row2b
```

## Other information

###### Annotations

* `is_input_aggregator: "true"`
