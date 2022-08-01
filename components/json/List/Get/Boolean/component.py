from kfp.components import create_component_from_func


def get_boolean_item_from_list(
    list: list,
    index: int,
) -> bool:
    """Gets item from a JSON array."""
    result = list[index]
    if not isinstance(result, bool):
        raise TypeError(f"Expected a boolean. Got {result}")
    return result


if __name__ == "__main__":
    get_boolean_item_from_list_op = create_component_from_func(
        get_boolean_item_from_list,
        base_image="python:3.10",
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Get/Boolean/component.yaml",
        },
    )
