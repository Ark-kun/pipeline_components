<!-- BEGIN_GENERATED_CONTENT -->
# Download data from IPFS

Description: Download data from IPFS using ipget.
See https://ipfs.io/
See https://github.com/ipfs/ipget

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/Download_and_upload/IPFS/Download/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/Download_and_upload/IPFS/Download/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Path** **\***|[String]||IPFS Path. Example: /ipfs/QmWATWQ7fVPP2EFGu71UkfnqhYXDYH566qy47CnJDgvs8u|

## Outputs

|Name|Type|Description|
|-|-|-|
|Data|||

## Implementation

#### Container

Container image: [alpine](https://hub.docker.com/r/_/)

## Usage

```python
download_data_from_IPFS_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/Download_and_upload/IPFS/Download/component.yaml")
...
download_data_from_IPFS_task = download_data_from_IPFS_op(
    path=...,
)
```

## Other information

###### Tags

* input_type=[String]

[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
