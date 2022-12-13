<!-- BEGIN_GENERATED_CONTENT -->
# Apply Kubernetes object

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/kubernetes/Apply_object/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/kubernetes/Apply_object/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Object** **\***|[JsonObject]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Name|[String]||
|Kind|[String]||
|Object|[JsonObject]||

## Implementation

#### Container

Container image: [bitnami/kubectl:1.17.17](https://hub.docker.com/r/bitnami/kubectl)

## Usage

```python
apply_Kubernetes_object_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/kubernetes/Apply_object/component.yaml")
...
apply_Kubernetes_object_task = apply_Kubernetes_object_op(
    object=...,
)
```

## Other information

###### Tags

* input_type=[JsonObject]
* output_type=[JsonObject]
* output_type=[String]

[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
