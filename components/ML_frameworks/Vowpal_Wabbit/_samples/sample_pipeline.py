from kfp import components

chicago_taxi_dataset_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/8dda6ec74d859a0112907fab8bc987a177b9fa4b/components/datasets/Chicago_Taxi_Trips/component.yaml")
pandas_transform_csv_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/pandas/Transform_DataFrame/in_CSV_format/component.yaml")
drop_header_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/tables/Remove_header/component.yaml")
calculate_regression_metrics_from_csv_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/37d98d43ad3193cf3516c134899f272d9643117c/components/ml_metrics/Calculate_regression_metrics/from_CSV/component.yaml")

create_Vowpal_Wabbit_dataset_from_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/a2a629e776d5fa0204ce71370cab23282d3e4278/components/ML_frameworks/Vowpal_Wabbit/Create_dataset/from_CSV/component.yaml")
create_Vowpal_Wabbit_JSON_dataset_from_CSV_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/a2a629e776d5fa0204ce71370cab23282d3e4278/components/ML_frameworks/Vowpal_Wabbit/Create_JSON_dataset/from_CSV/component.yaml")
train_regression_model_using_Vowpal_Wabbit_on_VowpalWabbitDataset_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/a2a629e776d5fa0204ce71370cab23282d3e4278/components/ML_frameworks/Vowpal_Wabbit/Train_regression_model/from_VowpalWabbitDataset/component.yaml")
train_regression_model_using_Vowpal_Wabbit_on_VowpalWabbitJsonDataset_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/a2a629e776d5fa0204ce71370cab23282d3e4278/components/ML_frameworks/Vowpal_Wabbit/Train_regression_model/from_VowpalWabbitJsonDataset/component.yaml")
predict_using_Vowpal_Wabbit_model_on_VowpalWabbitDataset_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/a2a629e776d5fa0204ce71370cab23282d3e4278/components/ML_frameworks/Vowpal_Wabbit/Predict/from_VowpalWabbitDataset/component.yaml")
predict_using_Vowpal_Wabbit_model_on_VowpalWabbitJsonDataset_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/a2a629e776d5fa0204ce71370cab23282d3e4278/components/ML_frameworks/Vowpal_Wabbit/Predict/from_VowpalWabbitJsonDataset/component.yaml")


def vowpal_wabbit_pipeline():
    training_data_csv = chicago_taxi_dataset_op(
        select="tips,trip_seconds,trip_miles,pickup_community_area,dropoff_community_area,fare,tolls,extras,trip_total"
    ).output

    training_data_vw = create_Vowpal_Wabbit_dataset_from_CSV_op(
        dataset=training_data_csv,
        label_column_name="tips",
    ).output

    # Testing dataset creation without label
    create_Vowpal_Wabbit_dataset_from_CSV_op(
        dataset=training_data_csv,
    ).output

    model1 = train_regression_model_using_Vowpal_Wabbit_on_VowpalWabbitDataset_op(
        dataset=training_data_vw,
    ).outputs["Model"]

    # Continue training
    model2 = train_regression_model_using_Vowpal_Wabbit_on_VowpalWabbitDataset_op(
        dataset=training_data_vw,
        initial_model=model1,
    ).outputs["Model"]

    # Predict
    predictions1 = predict_using_Vowpal_Wabbit_model_on_VowpalWabbitDataset_op(
        model=model1,
        dataset=training_data_vw,
    ).output
    predictions2 = predict_using_Vowpal_Wabbit_model_on_VowpalWabbitDataset_op(
        model=model2,
        dataset=training_data_vw,
    ).output

    # Calculating metrics
    # Preparing the true values
    true_values_table = pandas_transform_csv_op(
        table=training_data_csv,
        transform_code='''df = df[["tips"]]''',
    ).output

    true_values = drop_header_op(
        table=true_values_table,
    ).output

    # Calculating the regression metrics
    calculate_regression_metrics_from_csv_op(
        true_values=true_values,
        predicted_values=predictions1,
    )
    calculate_regression_metrics_from_csv_op(
        true_values=true_values,
        predicted_values=predictions2,
    )

    # Testing JSON datasets
    # Same training, but the dataset is now in JSON format
    training_data_vw_json = create_Vowpal_Wabbit_JSON_dataset_from_CSV_op(
        dataset=training_data_csv,
        label_column_name="tips",
    ).output

    # Testing dataset creation without label
    create_Vowpal_Wabbit_JSON_dataset_from_CSV_op(
        dataset=training_data_csv,
    ).output

    model3 = train_regression_model_using_Vowpal_Wabbit_on_VowpalWabbitJsonDataset_op(
        dataset=training_data_vw_json,
    ).outputs["Model"]

    predictions3 = predict_using_Vowpal_Wabbit_model_on_VowpalWabbitJsonDataset_op(
        model=model3,
        dataset=training_data_vw_json,
    ).output

    calculate_regression_metrics_from_csv_op(
        true_values=true_values,
        predicted_values=predictions3,
    )

if __name__ == "__main__":
    components.create_graph_component_from_pipeline_func(
        pipeline_func=vowpal_wabbit_pipeline,
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Vowpal_Wabbit/_samples/pipeline.component.yaml",
        },
        output_component_file="pipeline.component.yaml",
    )
