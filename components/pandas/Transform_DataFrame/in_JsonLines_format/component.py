from cloud_pipelines.components import InputPath, OutputPath, create_component_from_func


def transform_using_Pandas_DataFrame_on_JsonLines_data(
    table_path: InputPath("JsonLines"),
    transformed_table_path: OutputPath("JsonLines"),
    transform_code: "PythonCode",
):
    """Transform DataFrame loaded from an ApacheParquet file.

    Args:
        table_path: DataFrame to transform.
        transform_code: Transformation code. Code is written in Python and can consist of multiple lines.
            The DataFrame variable is called "df".
            Examples:
            - `df['prod'] = df['X'] * df['Y']`
            - `df = df[['X', 'prod']]`
            - `df.insert(0, "is_positive", df["X"] > 0)`
        transformed_table_path: Transformed DataFrame.
    """
    import pandas

    df = pandas.read_json(path_or_buf=table_path, lines=True)
    # The namespace is needed so that the code can replace `df`. For example df = df[['X']]
    namespace = dict(df=df)
    exec(transform_code, namespace)
    df = namespace["df"]
    df.to_json(path_or_buf=transformed_table_path, orient="records", lines=True)


if __name__ == "__main__":
    transform_using_Pandas_DataFrame_on_JsonLines_data_op = create_component_from_func(
        transform_using_Pandas_DataFrame_on_JsonLines_data,
        output_component_file="component.yaml",
        base_image="python:3.9",
        packages_to_install=[
            "pandas==1.4.3",
            "numpy<2",
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Transform_DataFrame/in_JsonLines_format/component.yaml",
        },
    )
