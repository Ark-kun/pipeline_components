from kfp import components

kfp_endpoint = None


run_component_or_pipeline_op = components.load_component_from_url('https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/kfp/Run_component/component.yaml')


def my_pipeline():
    run_component_or_pipeline_op(
        component_url='https://raw.githubusercontent.com/Ark-kun/pipeline_components/d8c4cf5e6403bc65bcf8d606e6baf87e2528a3dc/components/basics/Calculate_hash/component.yaml',
        arguments=dict(
            data='Hello world',
        ),
    )


if __name__ == '__main__':
    import kfp
    kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(my_pipeline, arguments={})
