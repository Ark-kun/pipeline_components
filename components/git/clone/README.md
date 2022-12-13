<!-- BEGIN_GENERATED_CONTENT -->
# Git clone

Description: Creates a shallow clone of the specified repo branch

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/git/clone/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/git/clone/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Repo URI** **\***|[URI]|||
|**Branch** **\***|[String]|master||

## Outputs

|Name|Type|Description|
|-|-|-|
|Repo dir|[Directory]||

## Implementation

#### Container

Container image: [alpine/git](https://hub.docker.com/r/)

## Usage

```python
git_clone_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/git/clone/component.yaml")
...
git_clone_task = git_clone_op(
    repo_uri=...,
    branch=...,
)
```

## Other information

###### Tags

* input_type=[String]
* input_type=[URI]
* output_type=[Directory]

[Directory]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Directory
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
[URI]: https://github.com/Ark-kun/pipeline_components/tree/master/types/URI
<!-- END_GENERATED_CONTENT -->
