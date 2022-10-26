from kfp.components import create_component_from_func


def create_dict_from_dict_value(
    key: str,
    value: dict,
) -> dict:
    """Creates a JSON object from key and value."""
    return {key: value}


if __name__ == "__main__":
    create_dict_from_dict_value_op = create_component_from_func(
        create_dict_from_dict_value,
        base_image="python:3.10",
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Create/from_Dict/component.yaml",
        },
    )
