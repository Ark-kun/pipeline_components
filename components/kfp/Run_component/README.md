<!-- BEGIN_GENERATED_CONTENT -->
# Run component or pipeline

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/kfp/Run_component/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/kfp/Run_component/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**component_url** **\***|[Url]|||
|**arguments** **\***|[JsonObject]|||
|endpoint|[String]|||
|wait_timeout_seconds|[Float]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|run_id|[String]||
|run_object|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
run_component_or_pipeline_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/kfp/Run_component/component.yaml")
...
run_component_or_pipeline_task = run_component_or_pipeline_op(
    component_url=...,
    arguments=...,
    # Optional:
    # endpoint=...,
    # wait_timeout_seconds=...,
)
```

## Other information

###### Tags

* input_type=[Float]
* input_type=[JsonObject]
* input_type=[String]
* input_type=[Url]
* output_type=[JsonObject]
* output_type=[String]

[Float]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Float
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[Url]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Url
<!-- END_GENERATED_CONTENT -->
