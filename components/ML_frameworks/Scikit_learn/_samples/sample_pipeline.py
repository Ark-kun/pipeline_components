from kfp import components

chicago_taxi_dataset_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/8dda6ec74d859a0112907fab8bc987a177b9fa4b/components/datasets/Chicago_Taxi_Trips/component.yaml")
pandas_transform_csv_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml")
drop_header_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml")
calculate_regression_metrics_from_csv_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/37d98d43ad3193cf3516c134899f272d9643117c/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml")

train_linear_regression_model_using_scikit_learn_from_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/f807e02b54d4886c65a05f40848fd51c72407f40/components/ML_frameworks/Scikit_learn/Train_linear_regression_model/from_CSV/component.yaml")
train_logistic_regression_model_using_scikit_learn_from_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/cb44b75c9c062fcc40c2b905b2024b4493dbc62b/components/ML_frameworks/Scikit_learn/Train_logistic_regression_model/from_CSV/component.yaml")
train_model_using_scikit_learn_from_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/46e8248ab69c6b7910b1eae05268493e4ec8ca90/components/ML_frameworks/Scikit_learn/Train_model/from_CSV/component.yaml")


def scikit_learn_linear_pipeline():
    raw_training_data_csv = chicago_taxi_dataset_op(
        select="tips,trip_seconds,trip_miles,pickup_community_area,dropoff_community_area,fare,tolls,extras,trip_total"
    ).output

    # Cleaning the NaN values.
    # Preventing ValueError: Input contains NaN, infinity or a value too large for dtype('float64').
    training_data_csv = pandas_transform_csv_op(
        table=raw_training_data_csv,
        transform_code='''df = df.fillna(0)''',
    ).output

    ## Linear regression
    linear_regression_model = train_linear_regression_model_using_scikit_learn_from_CSV_op(
        dataset=training_data_csv,
        label_column_name="tips",
    ).outputs["model"]

    ## Logistic regression
    # Replacing the float "tips" column with binary classification "any_tips" column
    binary_classification_training_data_csv = pandas_transform_csv_op(
        table=training_data_csv,
        transform_code='''df = pandas.concat([df.drop(columns=["tips"]), (df["tips"] > 0).replace({False: 0, True: 1}).rename("any_tips")], axis=1)''',
    ).output

    logistic_regression_model = train_logistic_regression_model_using_scikit_learn_from_CSV_op(
        dataset=binary_classification_training_data_csv,
        label_column_name="any_tips",
        # Optional:
        max_iterations=1000,
    ).outputs["model"]

    # Generic Scikit-learn model trainer
    linear_regression_model2 = train_model_using_scikit_learn_from_CSV_op(
        dataset=training_data_csv,
        label_column_name="tips",
        model_class_name="sklearn.linear_model.LinearRegression",
    ).outputs["model"]

    logistic_regression_model2 = train_model_using_scikit_learn_from_CSV_op(
        dataset=binary_classification_training_data_csv,
        label_column_name="any_tips",
        model_class_name="sklearn.linear_model.LogisticRegression",
        # Optional:
        model_parameters={"max_iter": 1000, "verbose": 1},
    ).outputs["model"]


if __name__ == "__main__":
    components.create_graph_component_from_pipeline_func(
        pipeline_func=scikit_learn_linear_pipeline,
        annotations={
           "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
           "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Scikit_learn/_samples/pipeline.component.yaml",
        },
        output_component_file="pipeline.component.yaml",
    )

if __name__ == "__main__":
    import os
    kfp_endpoint = os.environ.get("KFP_ENDPOINT") and os.environ.get("KFP_CREATE_RUN")
    if kfp_endpoint:
        import kfp
        kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(scikit_learn_linear_pipeline, arguments={})
