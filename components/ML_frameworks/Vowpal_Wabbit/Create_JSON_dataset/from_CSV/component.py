from kfp.components import InputPath, OutputPath, create_component_from_func


def create_Vowpal_Wabbit_JSON_dataset_from_CSV(
    dataset_path: InputPath("CSV"),
    converted_dataset_path: OutputPath("VowpalWabbitJsonDataset"),
    label_column_name: str = None,
):
    import json
    import pandas

    df = pandas.read_csv(dataset_path).convert_dtypes()

    if label_column_name:
        label_series = df[label_column_name]
        features_df = df.drop(columns=[label_column_name])
        label_values_list = label_series.to_list()
        feature_records_list = features_df.to_dict("records")

        with open(converted_dataset_path, "w") as f:
            for features, label in zip(feature_records_list, label_values_list):
                non_nan_features = {
                    k: v for k, v in features.items() if v == v and v is not None
                }
                vw_record = {
                    "_label": label,
                }
                vw_record.update(non_nan_features)
                vw_record_line = json.dumps(vw_record)
                f.write(vw_record_line + "\n")
    else:
        features_df = df
        feature_records_list = features_df.to_dict("records")

        with open(converted_dataset_path, "w") as f:
            for features in feature_records_list:
                non_nan_features = {
                    k: v for k, v in features.items() if v == v and v is not None
                }
                vw_record = non_nan_features
                vw_record_line = json.dumps(vw_record)
                f.write(vw_record_line + "\n")


if __name__ == "__main__":
    create_Vowpal_Wabbit_JSON_dataset_from_CSV_op = create_component_from_func(
        func=create_Vowpal_Wabbit_JSON_dataset_from_CSV,
        base_image="python:3.9",
        packages_to_install=["pandas==1.4.3", "numpy<2"],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Vowpal_Wabbit/Create_JSON_dataset/from_CSV/component.yaml",
        },
        output_component_file="component.yaml",
    )
