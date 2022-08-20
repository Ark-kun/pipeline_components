from typing import NamedTuple
from kfp.components import InputPath, OutputPath, create_component_from_func


def convert_column_to_categorical_using_Pandas_on_CSV_data(
    table_path: InputPath("CSV"),
    transformed_table_path: OutputPath("CSV"),
    column_name: str,
    categories: list = None,
) -> NamedTuple("Outputs", [("categories", list),]):
    """Replaces string values with category indexes.

    Args:
        column_name: Name of the column to convert
        categories: A list of category names that should be used to map string values to indexes.
            If omitted, the mapping will be automatically generated from the column unique values.
    """
    import pandas
    from pandas.api.types import CategoricalDtype

    df = pandas.read_csv(table_path).convert_dtypes()

    if not categories:
        print("The explicit list of categories was not passed, so inferring it automatically:")
        categories = sorted(df[column_name].dropna().unique())
        print(categories)

    categorical_type = CategoricalDtype(
        categories=categories,
        # ordered=True means that there is some number-like ordering for the categories.
        # In this case there is no ordering. This is not the same as sorted category names.
        ordered=False,
    )
    # Just changing the column type is not enough for CSV as the data would be written as strings.
    # We have to explicitly convert the column data to category indexes.
    df[column_name] = df[column_name].astype(categorical_type).cat.codes

    df.to_csv(
        transformed_table_path,
        index=False,
    )

    return (categories,)


if __name__ == "__main__":
    convert_column_to_categorical_using_Pandas_on_CSV_data_op = create_component_from_func(
        convert_column_to_categorical_using_Pandas_on_CSV_data,
        output_component_file="component.yaml",
        base_image="python:3.9",
        packages_to_install=[
            "pandas==1.4.3",
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Convert_column_to_categorical/in_CSV_format/component.yaml",
        },
    )
