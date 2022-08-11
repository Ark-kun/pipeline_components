from kfp.components import InputPath, OutputPath, create_component_from_func


def fill_all_missing_values_using_Pandas_on_ApacheParquet_data(
    table_path: InputPath("ApacheParquet"),
    transformed_table_path: OutputPath("ApacheParquet"),
    replacement_value: str = "0",
    replacement_type_name: str = "float",
):
    import builtins
    import pandas

    replacement_type = getattr(builtins, replacement_type_name)
    replacement_value = replacement_type(replacement_value)

    df = pandas.read_parquet(path=table_path)
    df = df.fillna(value=replacement_value)
    df.to_parquet(
        path=transformed_table_path, index=False,
    )


if __name__ == "__main__":
    fill_all_missing_values_using_Pandas_on_ApacheParquet_data_op = create_component_from_func(
        fill_all_missing_values_using_Pandas_on_ApacheParquet_data,
        output_component_file="component.yaml",
        base_image="python:3.9",
        packages_to_install=[
            "pandas==1.4.1",
            "pyarrow==9.0.0",
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Fill_all_missing_values/in_ApacheParquet_format/component.yaml",
        },
    )
