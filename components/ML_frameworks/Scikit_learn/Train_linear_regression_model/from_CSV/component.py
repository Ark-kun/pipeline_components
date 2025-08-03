from cloud_pipelines.components import InputPath, OutputPath, create_component_from_func


def train_linear_regression_model_using_scikit_learn_from_CSV(
    dataset_path: InputPath("CSV"),
    model_path: OutputPath("ScikitLearnPickleModel"),
    label_column_name: str,
):
    """Trains linear regression model using Scikit-learn.

    See https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression

    Args:
        dataset_path: Tabular dataset for training.
        model_path: Trained model in Scikit-learn pickle format.
        label_column_name: Name of the table column to use as label.
    """
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
            "numpy<2",
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Scikit_learn/Train_linear_regression_model/from_CSV/component.yaml",
        },
        output_component_file="component.yaml",
    )
