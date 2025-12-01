<!-- BEGIN_GENERATED_CONTENT -->
# Format date and time

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/basics/Format_date_time/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/basics/Format_date_time/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Date** **\***|[DateTime]|||
|**Format** **\***|[String]|%Y-%m-%d %H:%M:%S.%N|Format string for date and time. See [man date](https://linux.die.net/man/1/date).|

## Outputs

|Name|Type|Description|
|-|-|-|
|Formatted date|[String]||

## Implementation

#### Container

Container image: [ubuntu](https://hub.docker.com/r/_/)

## Usage

```python
format_date_and_time_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/basics/Format_date_time/component.yaml")
...
format_date_and_time_task = format_date_and_time_op(
    date=...,
    format=...,
)
```

## Other information

###### Tags

* input_type=[DateTime]
* input_type=[String]
* output_type=[String]

[DateTime]: https://github.com/Ark-kun/pipeline_components/tree/master/types/DateTime
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
