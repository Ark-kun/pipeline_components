from cloud_pipelines.components import InputPath, OutputPath, create_component_from_func


def predict_with_TensorFlow_model_on_ApacheParquet_data(
    dataset_path: InputPath("ApacheParquet"),
    model_path: InputPath("TensorflowSavedModel"),
    predictions_path: OutputPath(),
    label_column_name: str = None,
    batch_size: int = 1000,
):
    """Makes predictions using TensorFlow model.

    Args:
        dataset_path: Tabular dataset for prediction.
        model_path: Trained model in TensorFlow format.
        predictions_path: Predictions in multiline text format.
        label_column_name: Name of the table column to use as label.
        batch_size: Number of samples to use in each batch.
    """
    import numpy
    import tensorflow as tf
    import tensorflow_io as tfio

    FEATURES_COLUMN_NAME = "features"

    model = tf.saved_model.load(export_dir=model_path)

    def stack_feature_batches_and_drop_labels(columns_batch_dict):
        if label_column_name:
            # batch dict keys have bytes type
            columns_batch_dict.pop(label_column_name.encode())

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
        return features_batch

    # ! parquet::ParquetException is thrown if the Parquet dataset has nulls values
    dataset = tfio.IODataset.from_parquet(filename=dataset_path)

    dataset = dataset.batch(
        batch_size=batch_size,
        num_parallel_calls=tf.data.AUTOTUNE,
        deterministic=True,
    ).map(
        map_func=stack_feature_batches_and_drop_labels,
        num_parallel_calls=tf.data.AUTOTUNE,
        deterministic=True,
    )

    with open(predictions_path, "w") as predictions_file:
        for features_batch in dataset:
            predictions_tensor = model(features_batch)
            numpy.savetxt(predictions_file, predictions_tensor.numpy())


if __name__ == "__main__":
    predict_with_TensorFlow_model_on_ApacheParquet_data_op = create_component_from_func(
        predict_with_TensorFlow_model_on_ApacheParquet_data,
        output_component_file="component.yaml",
        base_image="tensorflow/tensorflow:2.9.1",
        packages_to_install=["tensorflow-io==0.26.0"],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/tensorflow/Predict/on_ApacheParquet/component.yaml",
        },
    )
