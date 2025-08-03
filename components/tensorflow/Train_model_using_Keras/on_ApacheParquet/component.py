from cloud_pipelines.components import create_component_from_func, InputPath, OutputPath


def train_model_using_Keras_on_ApacheParquet(
    training_data_path: InputPath("ApacheParquet"),
    model_path: InputPath("TensorflowSavedModel"),
    trained_model_path: OutputPath("TensorflowSavedModel"),
    label_column_name: str,
    loss_function_name: str = "mean_squared_error",
    number_of_epochs: int = 1,
    learning_rate: float = 0.1,
    optimizer_name: str = "Adadelta",
    optimizer_parameters: dict = None,
    batch_size: int = 32,
    metric_names: list = None,
    random_seed: int = 0,
):
    """Trains TensorFlow model.

    Args:
        training_data_path: Tabular dataset for training.
        model_path: Model in TensorFlow format.
        trained_model_path: Trained model in TensorFlow format.
        label_column_name: Name of the table column to use as label.
        loss_function_name: Name of the loss function.
        number_of_epochs: Number of training epochs.
        learning_rate: Learning rate of the optimizer.
        optimizer_name: Name of the optimizer.
        optimizer_parameters: Optimizer parameters in dictionary form.
        batch_size: Number of training samples to use in each batch.
        metric_names: A list of metrics to evaluate during the training.
        random_seed: Controls the seed of the random processes.
    """
    import tensorflow as tf
    import tensorflow_io as tfio

    tf.random.set_seed(seed=random_seed)

    FEATURES_COLUMN_NAME = "features"
    SHUFFLE_BUFFER_SIZE = 10000

    # Loading model using Keras. Model loaded using TensorFlow does not have .fit.
    # model = tf.saved_model.load(export_dir=model_path)
    keras_model = tf.keras.models.load_model(filepath=model_path)

    optimizer_parameters = optimizer_parameters or {}
    optimizer_parameters["learning_rate"] = learning_rate
    optimizer_config = {
        "class_name": optimizer_name,
        "config": optimizer_parameters,
    }
    optimizer = tf.keras.optimizers.get(optimizer_config)
    loss = tf.keras.losses.get(loss_function_name)

    def stack_feature_batches(columns_batch_dict):
        label_batch = columns_batch_dict.pop(label_column_name.encode())
        if FEATURES_COLUMN_NAME in columns_batch_dict:
            features_batch = columns_batch_dict[FEATURES_COLUMN_NAME]
        else:
            # Need to stack individual feature columns to create a single feature tensor
            # Need to cast all column tensor types to float
            list_of_feature_batches = list(
                tf.cast(x=feature_batch, dtype=tf.float32)
                for feature_batch in columns_batch_dict.values()
            )
            features_batch = tf.stack(list_of_feature_batches, axis=-1)
        return features_batch, label_batch

    # ! parquet::ParquetException is thrown if the Parquet dataset has nulls values
    training_dataset = tfio.IODataset.from_parquet(filename=training_data_path)

    training_dataset = (
        training_dataset.shuffle(buffer_size=SHUFFLE_BUFFER_SIZE, seed=random_seed)
        .repeat(count=number_of_epochs)
        .batch(
            batch_size=batch_size,
            num_parallel_calls=tf.data.AUTOTUNE,
            deterministic=True,
        )
        .map(
            map_func=stack_feature_batches,
            num_parallel_calls=tf.data.AUTOTUNE,
            deterministic=True,
        )
    )

    # Need to compile the model to prevent error:
    # ValueError: No gradients provided for any variable: [..., ...].
    keras_model.compile(
        optimizer=optimizer,
        loss=loss,
        metrics=metric_names,
    )
    keras_model.fit(
        training_dataset,
        epochs=number_of_epochs,
    )

    # Using tf.keras.models.save_model instead of tf.saved_model.save to prevent downstream error:
    # tf.saved_model.save(keras_model, trained_model_path)
    # ValueError: Unable to create a Keras model from this SavedModel.
    # This SavedModel was created with `tf.saved_model.save`, and lacks the Keras metadata.
    # Please save your Keras model by calling `model.save`or `tf.keras.models.save_model`.
    # See https://github.com/keras-team/keras/issues/16451
    tf.keras.models.save_model(keras_model, trained_model_path)


if __name__ == "__main__":
    train_model_using_Keras_on_ApacheParquet_op = create_component_from_func(
        train_model_using_Keras_on_ApacheParquet,
        output_component_file="component.yaml",
        base_image="tensorflow/tensorflow:2.8.0",
        # Check the version compatibility: https://github.com/tensorflow/io#tensorflow-version-compatibility
        packages_to_install=["tensorflow-io==0.25.0"],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/tensorflow/Train_model_using_Keras/on_ApacheParquet/component.yaml",
        },
    )
