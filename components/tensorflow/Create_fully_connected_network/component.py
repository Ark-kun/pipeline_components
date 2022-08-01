from kfp.components import create_component_from_func, OutputPath


def create_fully_connected_tensorflow_network(
    layer_sizes: list,
    model_path: OutputPath("TensorflowSavedModel"),
    activation_name: str = "relu",
    output_activation_name: str = None,
    random_seed: int = 0,
):
    """Creates fully-connected network in Tensorflow SavedModel format"""
    import tensorflow as tf
    tf.random.set_seed(seed=random_seed)

    if len(layer_sizes) < 2:
        raise ValueError(f"Fully-connected network requires at least two layer sizes (input and output). Got {layer_sizes}.")

    model = tf.keras.models.Sequential()
    model.add(tf.keras.Input(shape=(layer_sizes[0],)))
    for layer_size in layer_sizes[1:-1]:
        model.add(tf.keras.layers.Dense(units=layer_size, activation=activation_name))
    # The last layer is left without activation
    model.add(tf.keras.layers.Dense(units=layer_sizes[-1], activation=output_activation_name))

    # Using tf.keras.models.save_model instead of tf.saved_model.save to prevent downstream error:
    #tf.saved_model.save(model, model_path)
    # ValueError: Unable to create a Keras model from this SavedModel.
    # This SavedModel was created with `tf.saved_model.save`, and lacks the Keras metadata.
    # Please save your Keras model by calling `model.save`or `tf.keras.models.save_model`.
    # See https://github.com/keras-team/keras/issues/16451
    tf.keras.models.save_model(model, model_path)


if __name__ == "__main__":
    create_fully_connected_tensorflow_network_op = create_component_from_func(
        create_fully_connected_tensorflow_network,
        output_component_file="component.yaml",
        base_image="tensorflow/tensorflow:2.7.0",
        packages_to_install=[],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/tensorflow/Create_fully_connected_network/component.yaml",
        },
    )
