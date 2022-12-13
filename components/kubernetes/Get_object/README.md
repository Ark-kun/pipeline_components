<!-- BEGIN_GENERATED_CONTENT -->
# Get Kubernetes object

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/kubernetes/Get_object/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/kubernetes/Get_object/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Name** **\***|[String]|||
|**Kind** **\***|[String]|||

## Outputs

|Name|Type|Description|
|-|-|-|
|Object|[JsonObject]||

## Implementation

#### Container

Container image: [bitnami/kubectl:1.17.17](https://hub.docker.com/r/bitnami/kubectl)

## Usage

```python
get_Kubernetes_object_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/kubernetes/Get_object/component.yaml")
...
get_Kubernetes_object_task = get_Kubernetes_object_op(
    name=...,
    kind=...,
)
```

## Other information

###### Tags

* input_type=[String]
* output_type=[JsonObject]

[JsonObject]: https://github.com/Ark-kun/pipeline_components/tree/master/types/JsonObject
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
