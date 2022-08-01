from kfp.components import create_component_from_func


def append_list_item_to_list(
    list: list,
    item: list,
) -> list:
    """Append item to a JSON array."""
    list.append(item)
    return list


if __name__ == "__main__":
    append_list_item_to_list_op = create_component_from_func(
        append_list_item_to_list,
        base_image="python:3.10",
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Append/List/component.yaml",
        },
    )
