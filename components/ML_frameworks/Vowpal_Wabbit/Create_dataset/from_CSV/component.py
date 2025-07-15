from kfp.components import InputPath, OutputPath, create_component_from_func


def create_Vowpal_Wabbit_dataset_from_CSV(
    dataset_path: InputPath("CSV"),
    converted_dataset_path: OutputPath("VowpalWabbitDataset"),
    label_column_name: str = None,
    label_type: str = "simple_label",
):
    import pandas
    from vowpalwabbit import dftovw

    df = pandas.read_csv(dataset_path).convert_dtypes()
    # Hidden feature: Can pass multiple column names as comma-separated string.
    if label_column_name:
        label_columns = label_column_name.split(",")
        label_column_set = set(label_columns)
    else:
        label_column_set = set()
    label_column_list = sorted(list(label_column_set))
    feature_column_set = set(df.columns)
    feature_column_list = sorted(list(feature_column_set - label_column_set))
    # TODO: Simplify when https://github.com/VowpalWabbit/vowpal_wabbit/pull/3729 is merged and released.
    if label_column_name:
        converter = dftovw.DFtoVW.from_colnames(
            df=df, y=label_column_list, x=feature_column_list, label_type=label_type,
        )
    else:
        converter = dftovw.DFtoVW(
            df=df,
            features=[
                dftovw.Feature(value=feature_name)
                for feature_name in feature_column_list
            ],
        )

    converted_lines = converter.convert_df()
    with open(converted_dataset_path, "w") as f:
        for line in converted_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    create_Vowpal_Wabbit_dataset_from_CSV_op = create_component_from_func(
        func=create_Vowpal_Wabbit_dataset_from_CSV,
        base_image="python:3.9",
        packages_to_install=[
            "vowpalwabbit==9.0.1",
            "pandas==1.4.3",  # Not installed by vowpalwabbit despite its requirements.txt
            "numpy<2",
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Vowpal_Wabbit/Create_dataset/from_CSV/component.yaml",
        },
        output_component_file="component.yaml",
    )
