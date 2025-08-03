from cloud_pipelines.components import create_component_from_func


def merge_dicts(
    dict_1: dict = None,
    dict_2: dict = None,
    dict_3: dict = None,
    dict_4: dict = None,
    dict_5: dict = None,
) -> dict:
    """Merges multiple JSON objects into one."""
    result = {}
    for dict in [dict_1, dict_2, dict_3, dict_4, dict_5]:
        if dict is not None:
            result.update(dict)
    return result


if __name__ == "__main__":
    merge_dicts_op = create_component_from_func(
        merge_dicts,
        base_image="python:3.10",
        output_component_file="component.yaml",
        annotations={
            "author": "Alexey Volkov <alexey.volkov@ark-kun.com>",
            "canonical_location": "https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/json/Dict/Merge/component.yaml",
        },
    )
