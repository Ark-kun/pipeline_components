<!-- BEGIN_GENERATED_CONTENT -->
# Build integer parameter spec for Google Cloud AI Platform Optimizer

Description: Builds an instance of Google Cloud AI Platform Optimizer ParameterSpec.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Optimizer/Build_integer_parameter_spec/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Optimizer/Build_integer_parameter_spec/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**parameter** **\***|[String]||Name of teh parameter. The parameter name must be unique amongst all ParameterSpecs.|
|min_value|[Integer]|0|Minimum value of the parameter.|
|max_value|[Integer]|1|Maximum value of the parameter.|
|scale_type|[String]||The type of scaling that should be applied to this parameter.<br/>SCALE_TYPE_UNSPECIFIED By default, no scaling is applied.<br/>UNIT_LINEAR_SCALE Scales the feasible space to (0, 1) linearly.<br/>UNIT_LOG_SCALE Scales the feasible space logarithmically to (0, 1). The entire feasible space must be strictly positive.<br/>UNIT_REVERSE_LOG_SCALE Scales the feasible space "reverse" logarithmically to (0, 1). The result is that values close to the top of the feasible space are spread out more than points near the bottom. The entire feasible space must be strictly positive.|

## Outputs

|Name|Type|Description|
|-|-|-|
|parameter_spec|[JsonObject]||

## Implementation

#### Container

Container image: [python:3.9](https://hub.docker.com/r/_/python)

## Usage

```python
build_integer_parameter_spec_for_Google_Cloud_AI_Platform_Optimizer_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Optimizer/Build_integer_parameter_spec/component.yaml")
...
build_integer_parameter_spec_for_Google_Cloud_AI_Platform_Optimizer_task = build_integer_parameter_spec_for_Google_Cloud_AI_Platform_Optimizer_op(
    parameter=...,
    # Optional:
    # min_value=0,
    # max_value=1,
    # scale_type=...,
)
```

## Other information

###### Tags

* input_type=[Integer]
* input_type=[String]
* output_type=[JsonObject]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
