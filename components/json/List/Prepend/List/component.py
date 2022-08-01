from kfp.components import create_component_from_func


def prepend_list_item_to_list(
    list: list,
    item: list,
) -> list:
    """Prepend item to a JSON array."""
    list.insert(0, item)
    return list


if __name__ == "__main__":
    prepend_list_item_to_list_op = create_component_from_func(
        prepend_list_item_to_list,
        base_image="python:3.10",
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Prepend/List/component.yaml",
        },
    )
