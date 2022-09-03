from kfp.components import InputPath, OutputPath, create_component_from_func


def predict_with_TensorFlow_model_on_CSV_data(
    dataset_path: InputPath("CSV"),
    model_path: InputPath("TensorflowSavedModel"),
    predictions_path: OutputPath(),
    label_column_name: str = None,
    batch_size: int = 1000,
):
    import numpy
    import tensorflow as tf

    model = tf.saved_model.load(export_dir=model_path)

    dataset = tf.data.experimental.make_csv_dataset(
        file_pattern=dataset_path,
        batch_size=batch_size,
        label_name=label_column_name,
        header=True,
        num_epochs=1,
        shuffle=False,
        ignore_errors=False,
    )

    def stack_feature_batches(features_batch):
        # Need to stack individual feature columns to create a single feature tensor
        # Need to cast all column tensor types to float to prevent errors.
        list_of_feature_batches = list(
            tf.cast(x=feature_batch, dtype=tf.float32)
            for feature_batch in features_batch.values()
        )
        return tf.stack(list_of_feature_batches, axis=-1)

    def transform_features_and_drop_labels(features_batch, labels_batch):
        return stack_feature_batches(features_batch)

    dataset_map_fn = (
        transform_features_and_drop_labels
        if label_column_name
        else stack_feature_batches
    )

    dataset = dataset.map(dataset_map_fn)

    with open(predictions_path, "w") as predictions_file:
        for features_batch in dataset:
            predictions_tensor = model(features_batch)
            numpy.savetxt(predictions_file, predictions_tensor.numpy())


if __name__ == "__main__":
    predict_with_TensorFlow_model_on_CSV_data_op = create_component_from_func(
        predict_with_TensorFlow_model_on_CSV_data,
        output_component_file="component.yaml",
        base_image="tensorflow/tensorflow:2.9.1",
        packages_to_install=[],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/tensorflow/Predict/on_CSV/component.yaml",
        },
    )
