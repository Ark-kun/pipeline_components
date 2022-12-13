from kfp.components import InputPath, OutputPath, create_component_from_func


def binarize_column_using_Pandas_on_CSV_data(
    table_path: InputPath("CSV"),
    transformed_table_path: OutputPath("CSV"),
    column_name: str,
    predicate: str = "> 0",
    new_column_name: str = None,
    keep_original_column: bool = False,
):
    """Transforms a table column into a binary class column using a predicate.

    Args:
        table_path: Input data table.
        transformed_table_path: Transformed data table with the binary class column.
        column_name: Name of the column to transform to binary class.
        predicate: Expression that determines whether the column value is mapped to class 0 (false) or class 1 (true).
        new_column_name: Name for the new class column. Equals column_name by default.
        keep_original_column: Whether to keep the original column (column_name) in the table.
    """
    import pandas

    df = pandas.read_csv(table_path).convert_dtypes()
    original_series = df[column_name]

    # Dynamically executing the predicate code
    # Variable namespace for code execution
    namespace = dict(x=original_series)
    # I though that there should be no space before `predicate` so that "dot" predicate methods like ".between(min, max)" work.
    # However Python allows spaces before dot: `df .isna()`.
    # So having a space is not a problem
    transform_code = f"""new_series_boolean = x {predicate}"""
    # Note: exec() takes no keyword arguments
    # exec(__source=transform_code, __globals=namespace)
    exec(transform_code, namespace)
    new_series_boolean = namespace["new_series_boolean"]

    # There are multiple ways to convert boolean column to integer.
    # .apply(int) might be faster. https://stackoverflow.com/a/49804868/1497385
    # TODO: Do a proper benchmark.
    new_series = new_series_boolean.apply(int)
    # new_series = new_series_boolean.astype(int)
    # new_series = new_series_boolean.replace({False: 0, True: 1})

    if new_column_name:
        df.insert(loc=0, column=new_column_name, value=new_series)
        if not keep_original_column:
            df = df.drop(columns=[column_name])
    else:
        df[column_name] = new_series

    df.to_csv(transformed_table_path, index=False)


if __name__ == "__main__":
    binarize_column_using_Pandas_on_CSV_data_op = create_component_from_func(
        binarize_column_using_Pandas_on_CSV_data,
        output_component_file="component.yaml",
        base_image="python:3.9",
        packages_to_install=["pandas==1.4.3",],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Binarize_column/in_CSV_format/component.yaml",
        },
    )
