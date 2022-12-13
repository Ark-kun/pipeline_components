from kfp.components import InputPath, OutputPath, create_component_from_func


def select_columns_using_Pandas_on_ApacheParquet_data(
    table_path: InputPath("ApacheParquet"),
    transformed_table_path: OutputPath("ApacheParquet"),
    column_names: list,
):
    """Selects columns from a data table.

    Args:
        table_path: Input data table.
        transformed_table_path: Transformed data table that only has the chosen columns.
        column_names: Names of the columns to select from the table.
    """
    import pandas

    df = pandas.read_parquet(table_path)
    df = df[column_names]
    df.to_parquet(transformed_table_path, index=False)


if __name__ == "__main__":
    select_columns_using_Pandas_on_ApacheParquet_data_op = create_component_from_func(
        select_columns_using_Pandas_on_ApacheParquet_data,
        output_component_file="component.yaml",
        base_image="python:3.9",
        packages_to_install=[
            "pandas==1.4.1",
            "pyarrow==9.0.0",
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Select_columns/in_ApacheParquet_format/component.yaml",
        },
    )
