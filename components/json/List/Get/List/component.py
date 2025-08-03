from cloud_pipelines.components import create_component_from_func


def get_list_item_from_list(
    list: list,
    index: int,
) -> list:
    """Gets item from a JSON array."""
    result = list[index]
    if not isinstance(result, type([])):
        raise TypeError(f"Expected a list. Got {result}")
    return result


if __name__ == "__main__":
    get_list_item_from_list_op = create_component_from_func(
        get_list_item_from_list,
        base_image="python:3.10",
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Get/List/component.yaml",
        },
    )
