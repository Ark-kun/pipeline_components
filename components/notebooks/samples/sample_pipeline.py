kfp_endpoint = None

import kfp
from kfp import components

download_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/web/Download/component.yaml')
run_notebook_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/2b16a9f1331ef05da18f8b2b53707b7aa0f26662/components/notebooks/Run_notebook_using_papermill/component.yaml')

def notebook_pipeline():
    notebook = download_op('https://raw.githubusercontent.com/Ark-kun/pipeline_components/370224500e6b71fc9c25f05539e8f1ff49a47719/components/notebooks/samples/test_notebook.ipynb').output

    run_notebook_op(
        notebook=notebook,
        parameters={'param1': 'value 1'},
        input_data="Optional. Pass output of any component here. Can be a directory.",
        packages_to_install=["matplotlib"],
    )

if __name__ == '__main__':
    pipelin_run = kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(notebook_pipeline, arguments={})
