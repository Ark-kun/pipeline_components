from kfp.components import create_component_from_func


def get_size_of_dict(
    dict: dict,
) -> int:
    """Gets size of a JSON object."""
    return len(dict)


if __name__ == "__main__":
    get_size_of_dict_op = create_component_from_func(
        get_size_of_dict,
        base_image="python:3.10",
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Get_size/component.yaml",
        },
    )
