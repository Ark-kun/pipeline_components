from cloud_pipelines.components import InputPath, OutputPath, create_component_from_func


def convert_to_OnnxModel_from_ScikitLearnPickleModel(
    model_path: InputPath("ScikitLearnPickleModel"),
    converted_model_path: OutputPath("OnnxModel"),
    doc_string: str = "",
    target_opset: int = None,
):
    import onnx
    import pickle
    import skl2onnx

    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)

    # Funny hack to infer the model input shape
    # Just try passing arrays of different size to the model.predict method and check what works, lol.
    def get_input_output_shapes(model):
        for input_length_candidate in range(100000):
            try:
                prediction = model.predict(X=[[0.0] * input_length_candidate])
                input_length = input_length_candidate
                output_shape = prediction.shape[1:]
                return (input_length, output_shape)
            except:
                pass
        return None

    input_length, _ = get_input_output_shapes(model)

    # Setting model name is not necessary, but why not.
    model_type = type(model)
    model_type_name = model_type.__module__ + "." + model_type.__name__

    onnx_model = skl2onnx.convert_sklearn(
        model=model,
        initial_types=[
            ("input", skl2onnx.common.data_types.FloatTensorType([None, input_length]))
        ],
        name=model_type_name,
        verbose=1,
        # TODO: Include the original model hash digest so that the model can be traced.
        doc_string=doc_string,
        target_opset=target_opset,
    )
    print(onnx_model)
    onnx.save_model(
        proto=onnx_model, f=converted_model_path,
    )


if __name__ == "__main__":
    convert_to_OnnxModel_from_ScikitLearnPickleModel_op = create_component_from_func(
        func=convert_to_OnnxModel_from_ScikitLearnPickleModel,
        base_image="python:3.9",  # The onnx==1.11.0 package does not have wheels for Python 3.10 yet.
        packages_to_install=["skl2onnx==1.11"],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/_converters/ScikitLearnPickleModel/to_OnnxModel/component.yaml",
        },
        output_component_file="component.yaml",
    )
