<!-- BEGIN_GENERATED_CONTENT -->
# Run notebook using papermill

Description: Run Jupyter notebook using papermill.
The notebook will receive the parameter values passed to it as well as the INPUT_DATA_PATH and OUTPUT_DATA_PATH variables that will be set to the input data path (if provided) and directory for the optional output data.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/notebooks/Run_notebook_using_papermill/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/notebooks/Run_notebook_using_papermill/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Notebook** **\***|[JupyterNotebook]||Notebook to execute.|
|**Parameters** **\***|[JsonObject]|{}|Map with notebook paramater values.|
|**Packages to install** **\***|[JsonArray]||Python packages to install|
|Input data|||Optional data that can be passed to notebook. In notebook, the INPUT_DATA_PATH variable will point to the data (if passed).|

## Outputs

|Name|Type|Description|
|-|-|-|
|Notebook|[JupyterNotebook]|Executed notebook.|
|Output data||Directory with any output data. In notebook, the OUTPUT_DATA_PATH variable will point to this directory, so that the notebook can write output data there.|

## Implementation

#### Container

Container image: [python:3.7](https://hub.docker.com/r/_/python)

## Usage

```python
run_notebook_using_papermill_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/notebooks/Run_notebook_using_papermill/component.yaml")
...
run_notebook_using_papermill_task = run_notebook_using_papermill_op(
    notebook=...,
    parameters=...,
    packages_to_install=...,
    # Optional:
    # input_data=...,
)
```

## Other information

###### Tags

* input_type=[JsonArray]
* input_type=[JsonObject]
* input_type=[JupyterNotebook]
* output_type=[JupyterNotebook]

[JsonArray]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonArray
[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[JupyterNotebook]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JupyterNotebook
<!-- END_GENERATED_CONTENT -->
