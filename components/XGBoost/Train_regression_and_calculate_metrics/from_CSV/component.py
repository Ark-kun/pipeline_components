from collections import OrderedDict
from kfp import components


xgboost_train_on_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Train/component.yaml')
xgboost_predict_on_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/XGBoost/Predict/component.yaml')
pandas_transform_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml')
drop_header_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml')
calculate_regression_metrics_from_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml')


def xgboost_train_regression_and_calculate_metrics_on_csv(
    training_data: 'CSV',
    testing_data: 'CSV',
    label_column: int = 0,
    objective: str = 'reg:squarederror',
    num_iterations: int = 200,
):
    model = xgboost_train_on_csv_op(
        training_data=training_data,
        label_column=label_column,
        objective=objective,
        num_iterations=num_iterations,
    ).outputs['model']

    predictions = xgboost_predict_on_csv_op(
        data=testing_data,
        model=model,
        label_column=label_column,
    ).output

    true_values_table = pandas_transform_csv_op(
        table=testing_data,
        transform_code='df = df[["tips"]]',
    ).output

    true_values = drop_header_op(true_values_table).output

    metrics_task = calculate_regression_metrics_from_csv_op(
        true_values=true_values,
        predicted_values=predictions,
    )
    return OrderedDict([
        ('model', model),
        ('mean_absolute_error', metrics_task.outputs['mean_absolute_error']),
        ('mean_squared_error', metrics_task.outputs['mean_squared_error']),
        ('root_mean_squared_error', metrics_task.outputs['root_mean_squared_error']),
        ('metrics', metrics_task.outputs['metrics']),
    ])


if __name__ == '__main__':
    xgboost_train_regression_and_calculate_metrics_on_csv_op = components.create_graph_component_from_pipeline_func(
        xgboost_train_regression_and_calculate_metrics_on_csv,
        output_component_file='component.yaml',
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/XGBoost/Train_regression_and_calculate_metrics/from_CSV/component.yaml",
        },
    )
