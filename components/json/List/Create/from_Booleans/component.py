from kfp.components import create_component_from_func


def create_list_from_booleans(
    item_1: bool = None,
    item_2: bool = None,
    item_3: bool = None,
    item_4: bool = None,
    item_5: bool = None,
) -> list:
    """Creates a JSON array from booleans."""
    result = []
    for item in [item_1, item_2, item_3, item_4, item_5]:
        if item is not None:
            result.append(item)
    return result


if __name__ == "__main__":
    create_list_from_booleans_op = create_component_from_func(
        create_list_from_booleans,
        base_image="python:3.10",
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Create/from_Booleans/component.yaml",
        },
    )
