from kfp.components import InputPath, OutputPath, create_component_from_func


def convert_to_OnnxModel_from_XGBoostJsonModel(
    model_path: InputPath("XGBoostJsonModel"),
    converted_model_path: OutputPath("OnnxModel"),
    model_graph_name: str = None,
    doc_string: str = "",
    target_opset: int = None,
):
    import xgboost
    import onnx
    import onnxmltools

    # The file path needs to have .json extension so that the model is loaded as JSON format.
    import os
    import shutil
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=".json") as tmp_model_file:
        tmp_model_path = tmp_model_file.name
        shutil.copy(model_path, tmp_model_path)
        model = xgboost.Booster(model_file=tmp_model_path)

    # Workaround for https://github.com/onnx/onnxmltools/issues/499
    # Although I'm not sure this formula is correct given https://github.com/dmlc/xgboost/pull/6569
    model.best_ntree_limit = model.num_boosted_rounds()

    converted_model = onnxmltools.convert_xgboost(
        model=model,
        name=model_graph_name,
        initial_types=[
            (
                "input",
                onnxmltools.convert.common.data_types.FloatTensorType(
                    shape=[None, model.num_features()]
                ),
            )
        ],
        doc_string=doc_string,
        target_opset=target_opset,
    )
    onnx.save_model(proto=converted_model, f=converted_model_path)


if __name__ == "__main__":
    convert_to_OnnxModel_from_XGBoostJsonModel_op = create_component_from_func(
        func=convert_to_OnnxModel_from_XGBoostJsonModel,
        # onnx does not have wheels for Python 3.10 yet.
        base_image="python:3.9",
        packages_to_install=["xgboost==1.5.2", "onnx==1.11.0", "onnxmltools==1.10.0"],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/OnnxModel/from_XGBoostJsonModel/component.yaml",
        },
        output_component_file="component.yaml",
    )
