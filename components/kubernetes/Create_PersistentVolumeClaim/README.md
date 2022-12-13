<!-- BEGIN_GENERATED_CONTENT -->
# Create PersistentVolumeClaim in Kubernetes

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/kubernetes/Create_PersistentVolumeClaim/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/kubernetes/Create_PersistentVolumeClaim/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Name** **\***|[String]|||
|**Storage size** **\***|[String]|1Gi||

## Outputs

|Name|Type|Description|
|-|-|-|
|Name|[String]||

## Implementation

#### Container

Container image: [bitnami/kubectl:1.17.17](https://hub.docker.com/r/bitnami/kubectl)

## Usage

```python
create_PersistentVolumeClaim_in_Kubernetes_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/kubernetes/Create_PersistentVolumeClaim/component.yaml")
...
create_PersistentVolumeClaim_in_Kubernetes_task = create_PersistentVolumeClaim_in_Kubernetes_op(
    name=...,
    storage_size=...,
)
```

## Other information

###### Tags

* input_type=[String]
* output_type=[String]

[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
