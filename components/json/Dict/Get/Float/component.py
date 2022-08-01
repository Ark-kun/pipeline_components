from kfp.components import create_component_from_func


def get_float_item_from_dict(
    dict: dict,
    key: str,
) -> float:
    """Gets item from a JSON array."""
    result = dict[key]
    if not isinstance(result, float):
        raise TypeError(f"Expected a float. Got {result}")
    return result


if __name__ == "__main__":
    get_float_item_from_dict_op = create_component_from_func(
        get_float_item_from_dict,
        base_image="python:3.10",
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Get/Float/component.yaml",
        },
    )
