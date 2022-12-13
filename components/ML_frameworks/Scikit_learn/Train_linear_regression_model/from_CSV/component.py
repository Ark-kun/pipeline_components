from kfp.components import InputPath, OutputPath, create_component_from_func


def train_linear_regression_model_using_scikit_learn_from_CSV(
    dataset_path: InputPath("CSV"),
    model_path: OutputPath("ScikitLearnPickleModel"),
    label_column_name: str,
):
    import pandas
    import pickle
    from sklearn import linear_model

    df = pandas.read_csv(dataset_path)
    model = linear_model.LinearRegression()
    model.fit(
        X=df.drop(columns=label_column_name),
        y=df[label_column_name],
    )

    with open(model_path, "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    train_linear_regression_model_using_scikit_learn_from_CSV_op = create_component_from_func(
        func=train_linear_regression_model_using_scikit_learn_from_CSV,
        base_image="python:3.9",
        packages_to_install=[
            "scikit-learn==1.0.2",
            "pandas==1.4.3",
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Scikit_learn/Train_linear_regression_model/from_CSV/component.yaml",
        },
        output_component_file="component.yaml",
    )
