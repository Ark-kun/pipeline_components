<!-- BEGIN_GENERATED_CONTENT -->
# Delete Kubernetes object

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/kubernetes/Delete_object/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/kubernetes/Delete_object/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Name** **\***|[String]|||
|**Kind** **\***|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Name|[String]||
|Kind|[String]||

## Implementation

#### Container

Container image: [bitnami/kubectl:1.17.17](https://hub.docker.com/r/bitnami/kubectl)

## Usage

```python
delete_Kubernetes_object_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/kubernetes/Delete_object/component.yaml")
...
delete_Kubernetes_object_task = delete_Kubernetes_object_op(
    name=...,
    kind=...,
)
```

## Other information

###### Tags

* input_type=[String]
* output_type=[String]

[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
