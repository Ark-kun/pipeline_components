import json
import pathlib
from cloud_pipelines import components
# from cloud_pipelines.components import _naming
from cloud_pipelines._components.components import _naming



def github_raw_url_to_web_url(raw_url: str) -> str:
    # TODO: fix default branch name
    web_url = raw_url.replace("https://raw.githubusercontent.com/", "https://github.com/").replace("/master/", "/blob/master/")
    return web_url

def generate_readme(component_spec) -> str:
    result_lines = []
    result_lines.append("<!-- BEGIN_GENERATED_CONTENT -->")
    component_name = component_spec.name or "Component"
    result_lines.append(f"# {component_name}")
    result_lines.append("")
    if component_spec.description:
        result_lines.append("")
        result_lines.append(f"Description: {component_spec.description}")

    canonical_location = None
    if component_spec.metadata and component_spec.metadata.annotations:
        annotations = component_spec.metadata.annotations

        author_annotation = annotations.get("author")
        if author_annotation:
            result_lines.append("")
            result_lines.append(f"Author: {author_annotation}")
        canonical_location = annotations.get("canonical_location")
        if canonical_location:
            github_location = github_raw_url_to_web_url(canonical_location)
            result_lines.append("")
            result_lines.append(f"Location: [GitHub]({github_location}), [Raw]({canonical_location})")

    # result_lines.append("")
    # result_lines.append("## Interface")
    # result_lines.append("")

    input_types = set()
    output_types = set()

    if component_spec.inputs:
        result_lines.append("")
        result_lines.append("## Inputs")
        result_lines.append("")
        result_lines.append("|Name|Type|Default|Description|")
        result_lines.append("|-|-|-|-|")

    for input_spec in component_spec.inputs or []:
        formatted_input_name = input_spec.name
        if input_spec.optional:
            formatted_input_name = input_spec.name
        else:
            formatted_input_name = f"**{formatted_input_name}** **\\***"
        main_type_name, formatted_type = format_type(input_spec.type)
        if main_type_name:
            input_types.add(main_type_name)
        formatted_default = (input_spec.default or "").replace("\n", "<br/>")
        formatted_description = (input_spec.description or "").replace("\n", "<br/>")
        result_lines.append(
            f"""|{formatted_input_name}|{formatted_type}|{formatted_default}|{formatted_description}|"""
        )

    if component_spec.inputs:
        result_lines.append("")
        result_lines.append("## Outputs")
        result_lines.append("")
        result_lines.append("|Name|Type|Description|")
        result_lines.append("|-|-|-|")

    for output_spec in component_spec.outputs or []:
        main_type_name, formatted_type = format_type(output_spec.type)
        if main_type_name:
            output_types.add(main_type_name)
        formatted_description = (output_spec.description or "").replace("\n", "<br/>")
        result_lines.append(
            f"""|{output_spec.name}|{formatted_type}|{formatted_description}|"""
        )

    result_lines.append("")
    result_lines.append("## Implementation")
    result_lines.append("")

    container_spec = getattr(component_spec.implementation, "container", None)
    graph_spec = getattr(component_spec.implementation, "graph", None)

    if container_spec:
        #result_lines.append("")
        result_lines.append("#### Container")
        result_lines.append("")
        image_uri_parts = container_spec.image.split("/")
        if len(image_uri_parts) == 1:
            container_image_link = "https://hub.docker.com/r/_/" + container_spec.image.rpartition(":")[0]
        elif len(image_uri_parts) == 2:
            container_image_link = "https://hub.docker.com/r/" + container_spec.image.rpartition(":")[0]
        else:
            container_image_link = container_spec.image
        result_lines.append(f"Container image: [{container_spec.image}]({container_image_link})")
    if graph_spec:
        #result_lines.append("")
        result_lines.append("#### Graph")
        result_lines.append("")
        result_lines.append(f"##### Tasks")
        result_lines.append("")
        for task_id, task_spec in (graph_spec.tasks or {}).items():
            result_lines.append(f"""*   Task "{task_id}": Component [Web URL]({github_raw_url_to_web_url(task_spec.component_ref.url)}), [Raw URL]({task_spec.component_ref.url})""")

    ## Usage
    result_lines.append("")
    result_lines.append("## Usage")
    result_lines.append("")
    result_lines.append("```python")
    indent = " " * 4
    component_function_name = sanitize_python_function_name(component_name)
    if canonical_location:
        component_loading_code = f"""components.load_component_from_url("{canonical_location}")"""
    else:
        component_loading_code = f"""components.load_component_from_file("component.yaml")"""
    result_lines.append(f"{component_function_name}_op = {component_loading_code}")
    result_lines.append(f"...")
    result_lines.append(f"{component_function_name}_task = {component_function_name}_op(")
    optional_input_specs = []
    for input_spec in component_spec.inputs or []:
        python_input_name = _naming._sanitize_python_function_name(input_spec.name)
        if input_spec.optional:
            optional_input_specs.append(input_spec)
        else:
            result_lines.append(indent + f"{python_input_name}=...,")
    if optional_input_specs:
        result_lines.append(indent + f"# Optional:")
        for input_spec in optional_input_specs:
            python_input_name = _naming._sanitize_python_function_name(input_spec.name)
            default_value_string = "..."
            if input_spec.default:
                if input_spec.type == "Integer":
                    default_value_string = int(input_spec.default)
                elif input_spec.type == "Float":
                    default_value_string = float(input_spec.default)
                elif input_spec.type == "Boolean":
                    default_value_string = "True" if input_spec.default.lower() == "true" else "False"
                else:
                    default_value_string = '"' + input_spec.default.replace("\\", "\\\\").replace('"', '\"') + '"'
            else:
                if input_spec.type == "JsonArray":
                    default_value_string = "[...]"
                elif input_spec.type == "JsonObject":
                    default_value_string = "{...}"
            result_lines.append(indent + f"# {python_input_name}={default_value_string},")
    result_lines.append(f")")
    result_lines.append("```")

    result_lines.append("")
    result_lines.append("## Other information")
    result_lines.append("")

    # if component_spec.metadata and component_spec.metadata.annotations:
    #     if author_annotation:
    #         result_lines.append(f"Author: {author_annotation}")
    #     if canonical_location:
    #         result_lines.append(f"Canonical location: [link]({canonical_location})")


    #result_lines.append("")
    result_lines.append("###### Tags")
    result_lines.append("")
    for type_name in sorted(input_types):
        result_lines.append(f"* input_type=[{type_name}]")
    for type_name in sorted(output_types):
        result_lines.append(f"* output_type=[{type_name}]")

    # Type reference links (not visible)
    result_lines.append("")
    all_types = input_types | output_types
    for type_name in sorted(all_types):
        result_lines.append(
            f"[{type_name}]: https://github.com/Ark-kun/pipeline_components/tree/master/types/{type_name}"
        )

    result_lines.append("<!-- END_GENERATED_CONTENT -->")
    return "\n".join(result_lines).replace("\n\n\n", "\n\n") + "\n"


def format_type(type_spec) -> tuple:
    if not type_spec:
        return "", ""
    if isinstance(type_spec, str):
        main_type_name = type_spec
        type_attributes = {}
    elif isinstance(type_spec, dict):
        type_keys = list(type_spec.keys())
        assert len(type_keys) == 1
        main_type_name = type_keys[0]
        type_attributes = type_spec[main_type_name]
    else:
        raise TypeError(f"Unsupported type: {type_spec}")
    assert isinstance(type_attributes, dict)
    formatted_type = f"[{main_type_name}]"
    if type_attributes:
        formatted_type += f": `{json.dumps(type_attributes)}`"
    return main_type_name, formatted_type

def sanitize_python_function_name(name, lowercase=False):
    import re
    normalized_name = name
    if lowercase:
        normalized_name = name.lower()
    normalized_name = re.sub(r'[\W_]', ' ', normalized_name)        #No non-word characters
    normalized_name = re.sub(' +', ' ', normalized_name).strip()    #No double spaces, leading or trailing spaces
    if re.match(r'\d', normalized_name):
        normalized_name = 'n' + normalized_name                     #No leading digits
    normalized_name = normalized_name.replace(' ', '_')
    # Lower-casing the first letter
    normalized_name = normalized_name[0].lower() + normalized_name[1:]
    return normalized_name


if __name__ == "__main__":
    import sys
    #component_path = pathlib.Path("component.yaml")
    args = sys.argv[1:]
    if len(args) == 0:
        component_paths = ["component.yaml"]
    elif args[0] == "-":
        component_paths = (line.strip() for line in sys.stdin)
    else:
        component_paths = args

    for component_path in component_paths:
        print(component_path)
        try:
            component_path_obj = pathlib.Path(component_path)
            component = components.load_component_from_file(str(component_path_obj))
            component_spec = component.component_spec
            readme_text = generate_readme(component_spec)
            pathlib.Path(component_path_obj.parent / "README.md").write_text(readme_text)
        except Exception as ex:
            print(ex)
