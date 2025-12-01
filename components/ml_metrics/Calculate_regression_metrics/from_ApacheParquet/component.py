from typing import NamedTuple
from cloud_pipelines.components import InputPath, OutputPath, create_component_from_func


def calculate_regression_metrics_from_ApacheParquet(
    predictions_path: InputPath("ApacheParquet"),
    label_column_name: str = "label",
    prediction_column_name: str = "prediction",
) -> NamedTuple(
    "Outputs",
    [
        ("number_of_items", int),
        ("max_absolute_error", float),
        ("mean_absolute_error", float),
        ("mean_squared_error", float),
        ("root_mean_squared_error", float),
        ("metrics", dict),
    ],
):
    """Calculates regression metrics.

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>
    """
    import math
    import numpy

    import pandas

    df = pandas.read_parquet(predictions_path)

    true_values = df[label_column_name]
    predicted_values = df[prediction_column_name]

    if predicted_values.shape != true_values.shape:
        raise ValueError(
            "Input shapes are different: {} != {}".format(
                predicted_values.shape, true_values.shape
            )
        )

    number_of_items = true_values.size
    errors = true_values - predicted_values
    abs_errors = numpy.abs(errors)
    squared_errors = errors**2
    max_absolute_error = numpy.max(abs_errors).item()
    mean_absolute_error = numpy.average(abs_errors).item()
    mean_squared_error = numpy.average(squared_errors).item()
    root_mean_squared_error = math.sqrt(mean_squared_error)
    metrics = dict(
        number_of_items=number_of_items,
        max_absolute_error=max_absolute_error,
        mean_absolute_error=mean_absolute_error,
        mean_squared_error=mean_squared_error,
        root_mean_squared_error=root_mean_squared_error,
    )

    return (
        number_of_items,
        max_absolute_error,
        mean_absolute_error,
        mean_squared_error,
        root_mean_squared_error,
        metrics,
    )


if __name__ == "__main__":
    calculate_regression_metrics_from_ApacheParquet_op = create_component_from_func(
        calculate_regression_metrics_from_ApacheParquet,
        output_component_file="component.yaml",
        base_image="python:3.12",
        packages_to_install=["pandas==2.3.3", "pyarrow==22.0.0"],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ml_metrics/Calculate_regression_metrics/from_ApacheParquet/component.yaml",
            "python_dependencies_time": "2025-11-30",
        },
    )
