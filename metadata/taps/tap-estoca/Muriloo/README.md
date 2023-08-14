# tap-estoca

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md).

This tap:

- Pulls raw data from [Estoca's API](https://estoca.com.br/)
- Extracts the following resources:
  - Orders
- Outputs the schema for each resource
- Incrementally pulls data based on the input state 
- Do a full replication based on a start_date

## Context
Estoca is a logistics system used by small and medium companies in Brazil.

## Configuration

This tap requires a config.json which specifies details about Store ID, API Token and Start Date. An example of the config.json is as below:
```
{
  'storeID': '<a hash provided by Estoca's team>',
  'api_key': '<your token>',
  'start_date': '2020-12-01T00:00:00.000000Z'
}
```

## Streams

**orders**
- Endpoint: provided by Estoca's team
- Primary Key: id
- Replication strategy:
    - Incremental, based on 'updated_at' column
    - Do a request for each page until empty page is found
- Transformation:
    - Converts string 'None' returned by the API into python 'None'


---

Copyright &copy; 2020 Stitch
