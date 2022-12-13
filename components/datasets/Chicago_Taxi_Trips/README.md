<!-- BEGIN_GENERATED_CONTENT -->
# Chicago Taxi Trips dataset

Description: City of Chicago Taxi Trips dataset: https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew

The input parameters configure the SQL query to the database.
The dataset is pretty big, so limit the number of results using the `Limit` or `Where` parameters.
Read [Socrata dev](https://dev.socrata.com/docs/queries/) for the advanced query syntax

Author: Alexey Volkov <alexey.volkov@ark-kun.com>

Location: [GitHub](https://github.com/Ark-kun/pipeline_components/blob/master/components/datasets/Chicago_Taxi_Trips/component.yaml), [Raw](https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/datasets/Chicago_Taxi_Trips/component.yaml)

## Inputs

|Name|Type|Default|Description|
|-|-|-|-|
|**Where** **\***|[String]|trip_start_timestamp>="1900-01-01" AND trip_start_timestamp<"2100-01-01"||
|**Limit** **\***|[Integer]|1000|Number of rows to return. The rows are randomly sampled.|
|**Select** **\***|[String]|trip_id,taxi_id,trip_start_timestamp,trip_end_timestamp,trip_seconds,trip_miles,pickup_census_tract,dropoff_census_tract,pickup_community_area,dropoff_community_area,fare,tips,tolls,extras,trip_total,payment_type,company,pickup_centroid_latitude,pickup_centroid_longitude,pickup_centroid_location,dropoff_centroid_latitude,dropoff_centroid_longitude,dropoff_centroid_location||
|**Format** **\***|[String]|csv|Output data format. Supports csv,tsv,cml,rdf,json|

## Outputs

|Name|Type|Description|
|-|-|-|
|Table||Result type depends on format. CSV and TSV have header.|

## Implementation

#### Container

Container image: [byrnedo/alpine-curl@sha256:548379d0a4a0c08b9e55d9d87a592b7d35d9ab3037f4936f5ccd09d0b625a342](https://hub.docker.com/r/byrnedo/alpine-curl@sha256)

## Usage

```python
chicago_Taxi_Trips_dataset_op = components.load_component_from_url("https://raw.githubusercontent.com/Ark-kun/pipeline_components/master/components/datasets/Chicago_Taxi_Trips/component.yaml")
...
chicago_Taxi_Trips_dataset_task = chicago_Taxi_Trips_dataset_op(
    where=...,
    limit=...,
    select=...,
    format=...,
)
```

## Other information

###### Tags

* input_type=[Integer]
* input_type=[String]

[Integer]: https://github.com/Ark-kun/pipeline_components/tree/master/types/Integer
[String]: https://github.com/Ark-kun/pipeline_components/tree/master/types/String
<!-- END_GENERATED_CONTENT -->
