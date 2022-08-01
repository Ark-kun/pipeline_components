from kfp.components import create_component_from_func


def create_list_from_integers(
    item_1: int = None,
    item_2: int = None,
    item_3: int = None,
    item_4: int = None,
    item_5: int = None,
) -> list:
    """Creates a JSON array from integers."""
    result = []
    for item in [item_1, item_2, item_3, item_4, item_5]:
        if item is not None:
            result.append(item)
    return result


if __name__ == "__main__":
    create_list_from_integers_op = create_component_from_func(
        create_list_from_integers,
        base_image="python:3.10",
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/List/Create/from_Integers/component.yaml",
        },
    )
