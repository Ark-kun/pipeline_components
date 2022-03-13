from kfp.components import InputPath, OutputPath, create_component_from_func


def fill_all_missing_values_using_Pandas_on_CSV_data(
    table_path: InputPath("CSV"),
    transformed_table_path: OutputPath("CSV"),
    replacement_value: str = "0",
    replacement_type_name: str = "float",
):
    import builtins
    import pandas

    replacement_type = getattr(builtins, replacement_type_name)
    replacement_value = replacement_type(replacement_value)

    df = pandas.read_csv(table_path)
    df = df.fillna(value=replacement_value)
    df.to_csv(
        transformed_table_path, index=False,
    )


if __name__ == "__main__":
    fill_all_missing_values_using_Pandas_on_CSV_data_op = create_component_from_func(
        fill_all_missing_values_using_Pandas_on_CSV_data,
        output_component_file="component.yaml",
        base_image="python:3.9",
        packages_to_install=["pandas==1.4.1",],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Fill_all_missing_values/in_CSV_format/component.yaml",
        },
    )
