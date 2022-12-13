from kfp.components import InputPath, OutputPath, create_component_from_func


def train_model_using_scikit_learn_from_CSV(
    dataset_path: InputPath("CSV"),
    model_path: OutputPath("ScikitLearnPickleModel"),
    model_dict_path: OutputPath(dict),
    label_column_name: str,
    model_class_name: str,
    model_parameters: dict = {},
    random_seed: int = 0,
):
    """Train any Scikit-learn model

    Args:
        dataset_path: Tabular dataset for training.
        model_path: Trained model in Scikit-learn pickle format.
        model_dict_path: Trained model in dictionary format.
        label_column_name: Name of the table column to use as label.
        model_class_name: Full model class name. Example: `sklearn.linear_model.LogisticRegression`
        model_parameters: A dictionary of model class parameter values.
        random_seed: Controls the seed of the random processes.
    """
    import importlib
    import json
    import numpy
    import pandas
    import pickle
    import traceback

    model_class_module_name, model_class_class_name = model_class_name.rsplit(".", 1)

    model_module = importlib.import_module(model_class_module_name)
    model_class = getattr(model_module, model_class_class_name)

    numpy.random.seed(random_seed)
    model = model_class(**model_parameters)
    df = pandas.read_csv(dataset_path)
    model.fit(
        X=df.drop(columns=label_column_name),
        y=df[label_column_name],
    )
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    def default_serializer(x):
        type_name = type(x).__name__
        if type_name == "ndarray":
            return x.tolist()
        raise TypeError(
            f"TypeError: Object of type {type_name} is not JSON serializable"
        )

    # Including the model class name in the model dict
    model_dict = {"__class__": model_class_name}
    model_dict.update(model.__dict__)
    with open(model_dict_path, "w") as f:
        try:
            json.dump(
                obj=model_dict, fp=f, indent=2, default=default_serializer,
            )
        except:
            traceback.print_exc()


if __name__ == "__main__":
    train_model_using_scikit_learn_from_CSV_op = create_component_from_func(
        func=train_model_using_scikit_learn_from_CSV,
        base_image="python:3.9",
        packages_to_install=["scikit-learn==1.0.2", "pandas==1.4.3",],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Scikit_learn/Train_model/from_CSV/component.yaml",
        },
        output_component_file="component.yaml",
    )
