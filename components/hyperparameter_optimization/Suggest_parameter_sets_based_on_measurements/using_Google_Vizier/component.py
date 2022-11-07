from typing import NamedTuple

from kfp.components import create_component_from_func


def suggest_parameter_sets_based_on_measurements_using_google_vizier(
    parameter_specs: list,
    metrics_for_parameter_sets: list,
    suggestion_count: int,
    algorithm: str = "GRID_SEARCH",
    algorithm_config: dict = None,
    maximize: bool = False,
    metric_specs: list = None,
) -> NamedTuple("Outputs", [
    ("suggested_parameter_sets", list),
]):
    """Suggests parameter sets to evaluate based on the past measurements.

    See https://github.com/google/vizier/

    Args:
        parameter_specs: List of parameter specs. See https://github.com/google/vizier/blob/e92ab53bce139c89aff8c1590122c6b22adb5f47/vizier/service/study.proto#L171
        metrics_for_parameter_sets: List of parameter sets and evaluation metrics for them.
            Each list item contains "parameters" dict and "metrics" dict.
            Example: [{"parameters": {"p1": 1.1, "p2": 2.2}, "metrics": {"metric1": 101, "metric2": 102}}]
        suggestion_count: Number of suggestions to request.
        algorithm: The suggestion algorithm to use.
            Supported values: RANDOM_SEARCH, QUASI_RANDOM_SEARCH, GRID_SEARCH, NSGA2, EMUKIT_GP_EI, BOCS, HARMONICA, CMA_ES.
            See https://github.com/google/vizier/blob/4d4c3c517316c9650ad6e45dce0985fc609357e9/vizier/_src/pyvizier/oss/study_config.py#L45
        algorithm_config: Configuration of the chosen algorithm (as a dictionary).
        maximize: Whether to miaximize or minimize when optimizing a single metric. Default is to minimize. Ignored if metric_specs list is provided.
        metric_specs: List of metric specs. See https://github.com/google/vizier/blob/e92ab53bce139c89aff8c1590122c6b22adb5f47/vizier/service/study.proto#L150

        suggested_parameter_sets: List of parameter set dictionaries.
    """
    from google.protobuf import json_format
    import vizier
    import vizier.pyvizier
    import vizier.service.pyvizier
    import vizier.algorithms
    from vizier.service import study_pb2 as vizier_study_pb2

    # Handling metric specs
    # See https://github.com/google/vizier/blob/e92ab53bce139c89aff8c1590122c6b22adb5f47/vizier/service/study.proto#L150
    if metric_specs:
        # Converting from the old Google Cloud AI Platform Vizier format
        # See https://cloud.google.com/ai-platform/optimizer/docs/reference/rest/v1/projects.locations.studies#metricspec
        # See https://cloud.google.com/vertex-ai/docs/reference/rest/v1/StudySpec#metricspec
        for metric_spec in metric_specs:
            if "metric" in metric_spec:
                metric_spec["metric_id"] = metric_spec["metric"]
                del metric_spec["metric"]
    else:
        metric_specs = [
            {
                "metric_id": "metric",
                "goal": "MAXIMIZE" if maximize else "MINIMIZE",
            }
        ]
    # Handling parameter specs
    # See https://github.com/google/vizier/blob/e92ab53bce139c89aff8c1590122c6b22adb5f47/vizier/service/study.proto#L171
    # Converting from the old Google Cloud AI Platform Vizier format
    # See https://cloud.google.com/ai-platform/optimizer/docs/reference/rest/v1/projects.locations.studies#parameterspec
    # See https://cloud.google.com/vertex-ai/docs/reference/rest/v1/StudySpec#parameterspec
    for parameter_spec in parameter_specs:
        if "parameter" in parameter_spec:
            parameter_spec["parameter_id"] = parameter_spec["parameter"]
            del parameter_spec["parameter"]
        if "type" in parameter_spec:
            del parameter_spec["type"]

    # See https://github.com/google/vizier/blob/e92ab53bce139c89aff8c1590122c6b22adb5f47/vizier/service/study.proto#L148
    # See https://cloud.google.com/vertex-ai/docs/reference/rest/v1/StudySpec
    study_spec_dict = {
        "parameters": parameter_specs,
        "metrics": metric_specs,
    }

    # Preparing the existing measurements
    list_of_completed_trials = []
    for metrics_for_parameter_set in metrics_for_parameter_sets:
        parameter_set = metrics_for_parameter_set["parameters"]
        metrics = metrics_for_parameter_set["metrics"]
        completed_trial = vizier.pyvizier.Trial(
            parameters=parameter_set,
            final_measurement=vizier.pyvizier.Measurement(
                metrics=metrics,
            ),
        )
        list_of_completed_trials.append(completed_trial)
    completed_trials = vizier.algorithms.CompletedTrials(
        completed=list_of_completed_trials
    )

    # Preparing the algorithm (instance of a class derived from vizier.algorithms.Designer)
    algorithm_config = algorithm_config or {}

    study_spec = vizier_study_pb2.StudySpec()
    json_format.ParseDict(js_dict=study_spec_dict, message=study_spec)
    study_config = vizier.service.pyvizier.StudyConfig.from_proto(study_spec)
    problem_statement = study_config
    search_space = problem_statement.search_space

    def get_algorithm_designer(algorithm: str, algorithm_config: dict):
        if algorithm in ("ALGORITHM_UNSPECIFIED", "RANDOM_SEARCH"):
            from vizier._src.algorithms.policies import random_policy

            class RandomDesigner(vizier.algorithms.Designer):
                # policy = random_policy.RandomPolicy(policy_supporter=None)
                pass

            raise NotImplementedError
        elif algorithm == "QUASI_RANDOM_SEARCH":
            from vizier._src.algorithms.designers import quasi_random

            return quasi_random.QuasiRandomDesigner(
                search_space=search_space, **algorithm_config
            )
        elif algorithm == "GRID_SEARCH":
            from vizier._src.algorithms.designers import grid

            return grid.GridSearchDesigner(
                search_space=search_space, **algorithm_config
            )
        elif algorithm == "NSGA2":
            from vizier._src.algorithms.evolution import nsga2

            return nsga2.create_nsga2(problem=problem_statement, **algorithm_config)
        elif algorithm == "EMUKIT_GP_EI":
            from vizier._src.algorithms.designers import emukit

            return emukit.EmukitDesigner(
                study_config=problem_statement, **algorithm_config
            )
        elif algorithm == "BOCS":
            from vizier._src.algorithms.designers import bocs

            return bocs.BOCSDesigner(
                problem_statement=problem_statement, **algorithm_config
            )
        elif algorithm == "HARMONICA":
            from vizier._src.algorithms.designers import harmonica

            return harmonica.HarmonicaDesigner(
                problem_statement=problem_statement, **algorithm_config
            )
        elif algorithm == "CMA_ES":
            from vizier._src.algorithms.designers import cmaes

            return cmaes.CMAESDesigner(
                problem_statement=problem_statement, **algorithm_config
            )
        else:
            raise ValueError(f"Algorithm {algorithm} is not registered.")

    algorithm_designer = get_algorithm_designer(
        algorithm=algorithm, algorithm_config=algorithm_config
    )
    print(f"Using the {algorithm_designer.__class__} algorithm")

    # Feeding the existing measurements to the designer
    # Vizier bug: https://github.com/google/vizier/commit/f2c850568e42a9ef26332dd5e81f9ee26ff76a5d#r89004918
    # algorithm_designer.update(delta=completed_trials)
    algorithm_designer.update(completed_trials)

    # Getting suggestions
    suggested_trials = algorithm_designer.suggest(count=suggestion_count)
    suggested_parameter_sets = [
        trial.parameters.as_dict() for trial in suggested_trials
    ]

    return (suggested_parameter_sets,)


if __name__ == "__main__":
    suggest_parameter_sets_based_on_measurements_using_google_vizier_op = create_component_from_func(
        suggest_parameter_sets_based_on_measurements_using_google_vizier,
        base_image="python:3.10",
        packages_to_install=["google-vizier[algorithms]==0.0.13"],
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/hyperparameter_optimization/Suggest_parameter_sets_based_on_measurements/using_Google_Vizier/component.yaml",
        },
    )
