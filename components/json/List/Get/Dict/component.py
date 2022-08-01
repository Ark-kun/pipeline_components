from kfp.components import create_component_from_func


def get_dict_item_from_list(
    list: list,
    index: int,
) -> dict:
    """Gets item from a JSON array."""
    result = list[index]
    if not isinstance(result, dict):
        raise TypeError(f"Expected a dict. Got {result}")
    return result


if __name__ == "__main__":
    get_dict_item_from_list_op = create_component_from_func(
        get_dict_item_from_list,
        base_image="python:3.10",
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Get/Dict/component.yaml",
        },
    )
