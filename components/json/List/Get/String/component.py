from cloud_pipelines.components import create_component_from_func


def get_string_item_from_list(
    list: list,
    index: int,
) -> str:
    """Gets item from a JSON array."""
    result = list[index]
    if not isinstance(result, str):
        raise TypeError(f"Expected a string. Got {result}")
    return result


if __name__ == "__main__":
    get_string_item_from_list_op = create_component_from_func(
        get_string_item_from_list,
        base_image="python:3.10",
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Get/String/component.yaml",
        },
    )
