<!-- BEGIN_GENERATED_CONTENT -->
# Download data

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/web/Download/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/web/Download/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Url** **\***|[URI]|||
|**curl options** **\***|[string]|--location|Additional options given to the curl bprogram. See https://curl.haxx.se/docs/manpage.html|

## Outputs

|Name|Type|Description|
|-|-|-|
|Data|||

## Implementation

#### Container

Container image: [byrnedo/alpine-curl@sha256:548379d0a4a0c08b9e55d9d87a592b7d35d9ab3037f4936f5ccd09d0b625a342](https://hub.docker.com/r/byrnedo/alpine-curl@sha256)

## Usage

```python
download_data_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/web/Download/component.yaml")
...
download_data_task = download_data_op(
    url=...,
    curl_options=...,
)
```

## Other information

###### Tags

* input_type=[URI]
* input_type=[string]

[URI]: https://github.com/Ark-kun/pipeline_components/tree/master/types/URI
[string]: https://github.com/Ark-kun/pipeline_components/tree/master/types/string
<!-- END_GENERATED_CONTENT -->
