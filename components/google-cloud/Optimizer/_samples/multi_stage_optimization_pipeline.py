# This pipeline demonstrates hyper-parameter optimization.
# This version of the optimization pipeline uses imperative components that are closer to the API but not pure, so their usage is not recommended.
# Please use the google-cloud/Optimizer/Suggest_parameter_sets_based_on_measurements component
# and the atomic pipeline https://github.com/Ark-kun/pipeline_components/blob/master/components/google-cloud/Optimizer/_samples/multi_stage_optimization_atomic_pipeline.py
# instead.

kfp_endpoint = None

import datetime
import kfp
from kfp import components

optimizer_create_study_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/b3ec80d64938960d8caa4f1ba1ae1bbcc583e0b2//components/google-cloud/Optimizer/Create_study/component.yaml')
optimizer_suggest_trials_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/b3ec80d64938960d8caa4f1ba1ae1bbcc583e0b2//components/google-cloud/Optimizer/Suggest_trials/component.yaml')
optimizer_add_measurement_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/b3ec80d64938960d8caa4f1ba1ae1bbcc583e0b2//components/google-cloud/Optimizer/Add_measurement_for_trial/component.yaml')

get_element_by_index_op = components.load_component_from_url('https://raw.githubusercontent.com/kubeflow/pipelines/55ef28a9d51edc4eeed2a5c6f44cc7457e8a41d8/components/json/Get_element_by_index/component.yaml')
get_element_by_key_op = components.load_component_from_url('https://raw.githubusercontent.com/kubeflow/pipelines/55ef28a9d51edc4eeed2a5c6f44cc7457e8a41d8/components/json/Get_element_by_key/component.yaml')
query_json_op = components.load_component_from_url('https://raw.githubusercontent.com/kubeflow/pipelines/55ef28a9d51edc4eeed2a5c6f44cc7457e8a41d8/components/json/Query/component.yaml')


# Component that builds a model given the [hyper]parameters and evaluates that model.
# In this case, the model is a polynomial model.
# The evaluation procedure compares the model with the real function that our model is trying to learn
# and calculates the mean squared error based on a random sample of data points.
# In real world cases this component will be substituted by a sequence of model trainer, predictor and evaluator components.
@components.create_component_from_func
def evaluate_model(parameters: dict) -> float:
    import random

    def real_function(x):
        p1 = 3
        p2 = -1
        p3 = 2
        return p1 * x**2 + p2 * x + p3

    def evaluate_model(parameters, x):
        return parameters['p1'] * x**2 + parameters['p2'] * x + parameters['p3']

    sum_squared_error = 0
    num_samples = 100
    for i in range(num_samples):
        x = random.normalvariate(0, 1) * 5
        real_y = real_function(x)
        actual_y = evaluate_model(parameters, x)
        error = abs(real_y - actual_y)
        squared_error = error ** 2
        sum_squared_error += squared_error
    mean_squared_error = sum_squared_error / num_samples
    return mean_squared_error


def optimizer_pipeline(
):
    optimization_stages = 3
    trials_per_stage = 5
    study_id='Study_' + datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")

    study_name = optimizer_create_study_op(
        study_id=study_id,
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
        ],
        optimization_goal='MINIMIZE',
    ).outputs['study_name']

    # We launch several optimization stages sequentially.
    # Each stage depends on the completion of all trials in the previous stage (since only completed trials affect new trial suggesions).
    # Each optimization stage should result in better parameter set suggestions.
    trial_measurement_tasks = []
    for stage in range(optimization_stages):
        suggest_trials_task = optimizer_suggest_trials_op(
            study_name=study_name,
            suggestion_count=trials_per_stage,
        )
        suggest_trials_task.after(*trial_measurement_tasks)

        trials = suggest_trials_task.output

        # Evaluate each suggested set of parameters.
        # Loop over the suggested trials.
        # We need to collect the created tasks in the `trial_measurement_tasks` list so that the next round of suggestions can depend on their completion.
        # Cannot use dsl.ParallelFor here due to a bug in Argo https://github.com/argoproj/argo/issues/2660
        # Without ParallelFor we have to use python loop
        # and explicitly get individual suggestions using the get_element_by_index_op component
        # then extract the trial name and parameter sets using get_element_by_key_op and query_json_op components.
        trial_measurement_tasks = []
        for trial_index in range(trials_per_stage):
            trial = get_element_by_index_op(
                json=trials,
                index=trial_index,
            ).output

            trial_name = get_element_by_key_op(
                json=trial,
                key='name',
            ).output

            trial_parameters = query_json_op(
                json=trial,
                query='.parameters | map( {(.parameter): (.floatValue // .intValue // .stringValue)} ) | add',
            ).output

            model_error = evaluate_model(
                parameters=trial_parameters,
            ).output

            add_measurement_task = optimizer_add_measurement_op(
                trial_name=trial_name,
                metric_value=model_error,
            )

            trial_measurement_tasks.append(add_measurement_task)
    

if __name__ == '__main__':
    kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(optimizer_pipeline, arguments={})
