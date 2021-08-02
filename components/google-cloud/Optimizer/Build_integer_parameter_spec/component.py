from typing import NamedTuple

from kfp.components import create_component_from_func

def build_integer_parameter_spec_for_Google_Cloud_AI_Platform_Optimizer(
    parameter: str,
    min_value: int = 0,
    max_value: int = 1,
    scale_type: str = None,
) -> NamedTuple('Outputs', [
    ('parameter_spec', dict),
]):
    '''Builds an instance of Google Cloud AI Platform Optimizer ParameterSpec.

    See https://cloud.google.com/ai-platform/optimizer/docs/reference/rest/v1/projects.locations.studies#parameterspec

    Args:
        parameter: Name of teh parameter. The parameter name must be unique amongst all ParameterSpecs.
        min_value: Minimum value of the parameter.
        max_value: Maximum value of the parameter.
        scale_type: The type of scaling that should be applied to this parameter.
            SCALE_TYPE_UNSPECIFIED By default, no scaling is applied.
            UNIT_LINEAR_SCALE Scales the feasible space to (0, 1) linearly.
            UNIT_LOG_SCALE Scales the feasible space logarithmically to (0, 1). The entire feasible space must be strictly positive.
            UNIT_REVERSE_LOG_SCALE Scales the feasible space "reverse" logarithmically to (0, 1). The result is that values close to the top of the feasible space are spread out more than points near the bottom. The entire feasible space must be strictly positive.
    '''

    parameter_spec_dict = {
        "parameter": parameter,
        "type": "INTEGER",
        "integerValueSpec": {
            # Representing integers as strings: https://developers.google.com/discovery/v1/type-format
            "minValue": str(min_value),
            "maxValue": str(max_value),
        },
    }
    if scale_type:
        parameter_spec_dict["scaleType"] = scale_type

    return (parameter_spec_dict, )


if __name__ == '__main__':
    build_integer_parameter_spec_for_Google_Cloud_AI_Platform_Optimizer_op = create_component_from_func(
        build_integer_parameter_spec_for_Google_Cloud_AI_Platform_Optimizer,
        base_image='python:3.9',
        output_component_file='component.yaml',
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/google-cloud/Optimizer/Build_integer_parameter_spec/component.yaml",
        },
    )
