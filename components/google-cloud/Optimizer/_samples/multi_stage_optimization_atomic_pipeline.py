# This pipeline demonstrates hyper-parameter optimization.
# The goal is to find a set of hyper-parameter values that helps train the best model.
# We launch several optimization stages sequentially.
# At each stage the optimizer suggests several parameter sets to explore based on the available measurements.
# For each suggested parameter set we train a model (semi-dummy) and measure its quality metrics.
# We then collect the metrics for all suggested parameter sets and update out measurements set.
# With the expanded set of measurements, each new optimization stage should result in better parameter set suggestions.
#
# One aspect of this pipeline is the atomicity of the parameter set suggestion.
# Some optimizers have a persistent mutable global state that is changed when parameter set metrics are submitted.
# The presence of mutable global state may cause reproducibility issues where suggestions for a new model might be based on measurements from a different model.
# The "suggest_parameter_sets_from_measurements_op" in this pipeline is a single operation, which behaves like a pure function and does not rely on external global state.

import kfp
from kfp import components


suggest_parameter_sets_from_measurements_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/8469f9efd605c2a52e068e57894e01ff33a9d8b7/components/google-cloud/Optimizer/Suggest_parameter_sets_based_on_measurements/component.yaml')

get_item_from_list_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/4c166fc/components/json/List/Get/Dict/component.yaml')
create_dict_from_float_value_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/ef6979f5ff47df6e2375a1ce9e8c4d446b674e9f/components/json/Dict/Create/from_Float/component.yaml')
create_dict_from_dict_value_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/ef6979f5ff47df6e2375a1ce9e8c4d446b674e9f/components/json/Dict/Create/from_Dict/component.yaml')
merge_dicts_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/4c166fc/components/json/Dict/Merge/component.yaml')
create_list_from_dicts_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/4c166fc/components/json/List/Create/from_Dicts/component.yaml')
combine_lists_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/4c166fc/components/json/List/Combine/component.yaml')

# The train_and_measure_model is a semi-dummy component that creates a model given the [hyper]parameters and evaluates that model.
# In this case, the model is a polynomial model.
# The evaluation procedure compares the model with the real function that our model is trying to learn
# and calculates the mean squared error based on a random sample of data points.
# In real world cases this component will be substituted by a sequence of model trainer, predictor and evaluator components.
@components.create_component_from_func
def train_and_measure_model(parameters: dict) -> float:
    import random

    def real_function(x):
        p1 = 3
        p2 = -1
        p3 = 2
        return p1 * x**2 + p2 * x + p3

    def get_eval_set() -> dict:
        eval_set = {}
        num_samples = 100
        for i in range(num_samples):
            x = random.normalvariate(0, 1) * 5
            eval_set[x] = real_function(x)
        return eval_set

    def train_model(parameters):
        def apply_model(x):
            return parameters['p1'] * x**2 + parameters['p2'] * x + parameters['p3']
        return apply_model

    model = train_model(parameters)

    eval_set = get_eval_set()
    sum_squared_error = 0

    for x, expected_y in eval_set.items():
        actual_y = model(x)
        error = abs(expected_y - actual_y)
        squared_error = error ** 2
        sum_squared_error += squared_error
    mean_squared_error = sum_squared_error / len(eval_set)
    return mean_squared_error


parameter_specs=[
    {
        'parameter': 'p1',
        'type': 'DOUBLE',
        'double_value_spec' : {
            'min_value' : -5,
            'max_value' : 5,
        }
    },
    {
        'parameter': 'p2',
        'type': 'DOUBLE',
        'double_value_spec': {
            'min_value': -5,
            'max_value': 5,
        }
    },
    {
        'parameter': 'p3',
        'type': 'DOUBLE',
        'double_value_spec': {
            'min_value': -5,
            'max_value': 5,
        }
    },
]


def optimizer_pipeline():
    # Number of optimization stages and suggestions per stage.
    # Note that these numbers cannot be parametrized, since they're used in compile-time python loops.
    optimization_stages = 3
    suggestions_per_stage = 5

    # We launch several optimization stages sequentially.
    # At each stage the optimizer suggests several parameter sets to explore based on the available measurements.
    # Each stage depends on the completion of all trials in the previous stage (since only completed trials affect new trial suggesions).
    # Each optimization stage should result in better parameter set suggestions.
    all_metrics_for_parameter_sets = []
    for stage in range(optimization_stages):
        parameter_sets = suggest_parameter_sets_from_measurements_op(
            parameter_specs=parameter_specs,
            metrics_for_parameter_sets=all_metrics_for_parameter_sets,
            suggestion_count=suggestions_per_stage,
            maximize=False,
        ).output

        # Evaluate each suggested set of parameters.
        # Loop over the suggested trials.
        # We need to collect the created tasks in the `trial_measurement_tasks` list so that the next round of suggestions can depend on their completion.
        # Cannot use dsl.ParallelFor here due to a bug in Argo https://github.com/argoproj/argo-workflows/issues/2660
        # Without ParallelFor we have to use python loop
        # and explicitly get individual suggestions using the get_element_by_index_op component
        # then extract the trial name and parameter sets using get_element_by_key_op and query_json_op components.
        new_metrics_for_parameter_sets = []
        for siggestion_index in range(suggestions_per_stage):
            parameter_set = get_item_from_list_op(
                list=parameter_sets,
                index=siggestion_index,
            ).output

            model_error = train_and_measure_model(
                parameters=parameter_set,
            ).output

            metric_for_parameter_set = merge_dicts_op(
                dict_1=create_dict_from_dict_value_op(
                    key="parameters",
                    value=parameter_set,
                ).output,
                dict_2=create_dict_from_dict_value_op(
                    key="metrics",
                    value=create_dict_from_float_value_op(
                        key="metric",
                        value=model_error,
                    ).output,
                ).output,
            ).output

            new_metrics_for_parameter_sets.append(metric_for_parameter_set)
        # Collecting metrics for the current stage
        new_list_of_metrics_for_parameter_sets = create_list_from_dicts_op(*new_metrics_for_parameter_sets).output
        # Collecting metrics for all stages
        all_metrics_for_parameter_sets = combine_lists_op(all_metrics_for_parameter_sets, new_list_of_metrics_for_parameter_sets).output


pipeline_func = optimizer_pipeline


if __name__ == "__main__":
    import kfp
    # Set the KF_PIPELINES_ENDPOINT environment variable to the KFP endpoint URL:
    # import os; os.environ["KF_PIPELINES_ENDPOINT"] = "https://XXXXXXXXXXXXXXXX-dot-us-central2.pipelines.googleusercontent.com"
    kfp.Client().create_run_from_pipeline_func(pipeline_func, arguments={})
