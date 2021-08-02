from kfp.components import create_component_from_func


def build_list_of_floats(
    item_1: float = None,
    item_2: float = None,
    item_3: float = None,
    item_4: float = None,
    item_5: float = None,
) -> list:
    """Creates a JSON array from multiple floating-point numbers.

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>
    """
    result = []
    for item in [item_1, item_2, item_3, item_4, item_5]:
        if item is not None:
            result.append(item)
    return result


if __name__ == '__main__':
    build_list_of_floats_op = create_component_from_func(
        build_list_of_floats,
        base_image='python:3.8',
        output_component_file='component.yaml',
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Build_list_of_floats/component.yaml",
        },
    )
