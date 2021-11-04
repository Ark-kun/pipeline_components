from kfp.components import InputPath, OutputPath, create_component_from_func


def convert_to_XGBoostModel_from_XGBoostJsonModel(
    model_path: InputPath("XGBoostJsonModel"),
    converted_model_path: OutputPath("XGBoostModel"),
):
    import os
    import shutil
    import tempfile
    import xgboost

    # The file path needs to have .json extension so that the model is loaded as JSON format.
    with tempfile.NamedTemporaryFile(suffix=".json") as tmp_model_file:
        tmp_model_path = tmp_model_file.name
        shutil.copy(model_path, tmp_model_path)
        model = xgboost.Booster(model_file=tmp_model_path)

    tmp_converted_model_path = converted_model_path + ".bst"
    model.save_model(tmp_converted_model_path)
    os.rename(tmp_converted_model_path, converted_model_path)


if __name__ == "__main__":
    convert_to_XGBoostModel_from_XGBoostJsonModel_op = create_component_from_func(
        convert_to_XGBoostModel_from_XGBoostJsonModel,
        output_component_file="component.yaml",
        base_image="python:3.9",
        packages_to_install=[
            "xgboost==1.5.0",
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/XGBoostJsonModel/to_XGBoostModel/component.yaml",
        },
    )
