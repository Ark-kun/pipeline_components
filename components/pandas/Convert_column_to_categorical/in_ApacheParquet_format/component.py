from typing import NamedTuple
from kfp.components import InputPath, OutputPath, create_component_from_func


def convert_column_to_categorical_using_Pandas_on_ApacheParquet_data(
    table_path: InputPath("ApacheParquet"),
    transformed_table_path: OutputPath("ApacheParquet"),
    column_name: str,
    categories: list = None,
) -> NamedTuple("Outputs", [("categories", list),]):
    """Changes column type to categorical.

    Args:
        column_name: Name of the column to convert
        categories: A list of category names that should be used to map string values to indexes.
            If omitted, the mapping will be automatically generated from the column unique values.
    """
    import pandas
    from pandas.api.types import CategoricalDtype

    df = pandas.read_parquet(path=table_path)

    if not categories:
        print("The explicit list of categories was not passed, so inferring it automatically:")
        unique_items = df[column_name].dropna().unique()
        # ! Pandas' Series.unique() returns very different objects depending on the dtype !
        if hasattr(unique_items, "to_numpy"):
            unique_items = unique_items.to_numpy()
        # ! Using `.tolist()` is required to convert non-native types like numpy.int64
        # (that cannot be JSON-serialized by default) to Python native types like int.
        unique_items = unique_items.tolist()
        categories = sorted(unique_items)
        print(categories)

    categorical_type = CategoricalDtype(
        categories=categories,
        # ordered=True means that there is some number-like ordering for the categories.
        # In this case there is no ordering. This is not the same as sorted category names.
        ordered=False,
    )
    # Parquet supports the categorical column type natively.
    df[column_name] = df[column_name].astype(categorical_type)

    df.to_parquet(
        path=transformed_table_path,
        index=False,
    )

    return (categories,)


if __name__ == "__main__":
    convert_column_to_categorical_using_Pandas_on_ApacheParquet_data_op = create_component_from_func(
        convert_column_to_categorical_using_Pandas_on_ApacheParquet_data,
        output_component_file="component.yaml",
        base_image="python:3.9",
        packages_to_install=[
            "pandas==1.4.3",
            "pyarrow==9.0.0",
        ],
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/pandas/Convert_column_to_categorical/in_ApacheParquet_format/component.yaml",
        },
    )
