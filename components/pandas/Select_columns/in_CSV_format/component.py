from kfp.components import InputPath, OutputPath, create_component_from_func


def select_columns_using_Pandas_on_CSV_data(
    table_path: InputPath("CSV"),
    transformed_table_path: OutputPath("CSV"),
    column_names: list,
):
    import pandas

    df = pandas.read_csv(
        table_path,
        dtype="string",
    )
    df = df[column_names]
    df.to_csv(transformed_table_path, index=False)


if __name__ == "__main__":
    select_columns_using_Pandas_on_CSV_data_op = create_component_from_func(
        select_columns_using_Pandas_on_CSV_data,
        output_component_file="component.yaml",
        base_image="python:3.9",
        packages_to_install=["pandas==1.4.2",],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Select_columns/in_CSV_format/component.yaml",
        },
    )
