<!-- BEGIN_GENERATED_CONTENT -->
# Create Tensorboard visualization

Description: Pre-creates Tensorboard visualization for a given Log dir URI.
This way the Tensorboard can be viewed before the training completes.
The output Log dir URI should be passed to a trainer component that will write Tensorboard logs to that directory.

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/tensorflow/tensorboard/prepare_tensorboard/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/tensorflow/tensorboard/prepare_tensorboard/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Log dir URI** **\***||||

## Outputs

|Name|Type|Description|
|-|-|-|
|Log dir URI|||
|MLPipeline UI Metadata|||

## Implementation

#### Container

Container image: [alpine](https://hub.docker.com/r/_/)

## Usage

```python
create_Tensorboard_visualization_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/tensorflow/tensorboard/prepare_tensorboard/component.yaml")
...
create_Tensorboard_visualization_task = create_Tensorboard_visualization_op(
    log_dir_uri=...,
)
```

## Other information

###### Tags

<!-- END_GENERATED_CONTENT -->
