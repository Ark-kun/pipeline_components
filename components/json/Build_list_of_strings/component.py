from kfp.components import create_component_from_func


def build_list_of_strings(
    item_1: str = None,
    item_2: str = None,
    item_3: str = None,
    item_4: str = None,
    item_5: str = None,
) -> list:
    """Creates a JSON array from multiple strings.

    Annotations:
        author: Alexey Volkov <alexey.volkov@ark-kun.com>
    """
    result = []
    for item in [item_1, item_2, item_3, item_4, item_5]:
        if item is not None:
            result.append(item)
    return result


if __name__ == '__main__':
    build_list_of_strings_op = create_component_from_func(
        build_list_of_strings,
        base_image='python:3.9',
        output_component_file='component.yaml',
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Build_list_of_strings/component.yaml",
        },
    )
