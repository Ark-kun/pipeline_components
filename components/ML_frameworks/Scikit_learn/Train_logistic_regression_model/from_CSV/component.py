from typing import NamedTuple
from kfp.components import InputPath, OutputPath, create_component_from_func


def train_logistic_regression_model_using_scikit_learn_from_CSV(
    dataset_path: InputPath("CSV"),
    model_path: OutputPath("ScikitLearnPickleModel"),
    label_column_name: str,
    penalty: str = "l2", # l1, l2, elasticnet, none
    solver: str = "lbfgs", # newton-cg, lbfgs, liblinear, sag, saga
    max_iterations: int = 100,
    multi_class_mode: str = "auto", # auto, ovr, multinomial
    random_seed: int = 0,
) -> NamedTuple("Outputs", [
    ("model_parameters", dict),
]):
    """Trains logistic regression model using Scikit-learn.

    See https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

    Args:
        dataset_path: Tabular dataset for training.
        model_path: Trained model in Scikit-learn pickle format.
        label_column_name: Name of the table column to use as label.
        penalty: Used to specify the norm used in the penalization.
            Possible values: {'l1', 'l2', 'elasticnet', 'none'}, default='l2'
            The 'newton-cg',
            'sag' and 'lbfgs' solvers support only l2 penalties. 'elasticnet' is
            only supported by the 'saga' solver. If 'none' (not supported by the
            liblinear solver), no regularization is applied.
        solver: Algorithm to use in the optimization problem.
            Possible values: {'newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'}, default='lbfgs'

            - For small datasets, 'liblinear' is a good choice, whereas 'sag' and
            'saga' are faster for large ones.
            - For multiclass problems, only 'newton-cg', 'sag', 'saga' and 'lbfgs'
            handle multinomial loss; 'liblinear' is limited to one-versus-rest
            schemes.
            - 'newton-cg', 'lbfgs', 'sag' and 'saga' handle L2 or no penalty
            - 'liblinear' and 'saga' also handle L1 penalty
            - 'saga' also supports 'elasticnet' penalty
            - 'liblinear' does not support setting ``penalty='none'``

            Note that 'sag' and 'saga' fast convergence is only guaranteed on
            features with approximately the same scale. You can
            preprocess the data with a scaler from sklearn.preprocessing.
        max_iterations: Maximum number of iterations taken for the solvers to converge.
        multi_class_mode: Possible values: {'auto', 'ovr', 'multinomial'}, default='auto'
            If the option chosen is 'ovr', then a binary problem is fit for each
            label. For 'multinomial' the loss minimised is the multinomial loss fit
            across the entire probability distribution, *even when the data is
            binary*. 'multinomial' is unavailable when solver='liblinear'.
            'auto' selects 'ovr' if the data is binary, or if solver='liblinear',
            and otherwise selects 'multinomial'.
        random_seed: Controls the seed of the random processes.
    """
    import json
    import pandas
    import pickle
    from sklearn import linear_model

    df = pandas.read_csv(dataset_path)
    model = linear_model.LogisticRegression(
        penalty=penalty,
        #dual=False,
        #tol=1e-4,
        #C=1.0,
        #fit_intercept=True,
        #intercept_scaling=1,
        #class_weight=None,
        random_state=random_seed,
        solver=solver,
        max_iter=max_iterations,
        multi_class=multi_class_mode,
        #l1_ratio=None,
        verbose=1,
    )

    model_parameters = model.get_params()
    model_parameters_json = json.dumps(model_parameters, indent=2)
    print("Model parameters:")
    print(model_parameters_json)
    print()

    model.fit(
        X=df.drop(columns=label_column_name),
        y=df[label_column_name],
    )

    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    return (model_parameters_json,)


if __name__ == "__main__":
    train_logistic_regression_model_using_scikit_learn_from_CSV_op = create_component_from_func(
        func=train_logistic_regression_model_using_scikit_learn_from_CSV,
        base_image="python:3.9",
        packages_to_install=[
            "scikit-learn==1.0.2",
            "pandas==1.4.3",
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/ML_frameworks/Scikit_learn/Train_logistic_regression_model/from_CSV/component.yaml",
        },
        output_component_file="component.yaml",
    )
