from kfp.components import InputPath, OutputPath, create_component_from_func


def convert_to_XGBoostJsonModel_from_XGBoostModel(
    model_path: InputPath("XGBoostModel"),
    converted_model_path: OutputPath("XGBoostJsonModel"),
):
    import os
    import xgboost

    model = xgboost.Booster(model_file=model_path)

    # The file path needs to have .json extension so that the model is saved in the JSON format.
    tmp_converted_model_path = converted_model_path + ".json"
    model.save_model(tmp_converted_model_path)
    os.rename(tmp_converted_model_path, converted_model_path)


if __name__ == "__main__":
    convert_to_XGBoostJsonModel_from_XGBoostModel_op = create_component_from_func(
        convert_to_XGBoostJsonModel_from_XGBoostModel,
        output_component_file="component.yaml",
        base_image="python:3.9",
        packages_to_install=[
            "xgboost==1.5.0",
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/XGBoostJsonModel/from_XGBoostModel/component.yaml",
        },
    )
