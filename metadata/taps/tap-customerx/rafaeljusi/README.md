# tap-customerx

This is a [Singer](https://singer.io) tap that produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:
- Pulls raw data from CustomerX's [REST API](https://doc.api.customerx.com.br/?version=latest)
- Extracts the following resources from CustomerX
  - [Clientes](https://doc.api.customerx.com.br/?version=latest#a0803301-389b-45d5-a77b-43d413e7534b)
  - [NPS](https://doc.api.customerx.com.br/?version=latest#4655df85-aae7-47c8-a7d4-4def0494c956)
  - [Tasks](https://doc.api.customerx.com.br/?version=latest#a5412030-4ace-4ded-8e90-95ccc4f1725b)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

## setup

1. Install the tap
`pip install -e .`

2. Install the target
`pip install target-stitch`

3. Create and edit the tap config file (tap_config.json)
```
{
    "api_token": "YOUR_API_TOKEN",
    "start_date": "2017-01-01T00:00:00Z"
}
```

4. Create and edit the target config file (target_config.json)
```
{
    "client_id" : YOUR_CLIENT_ID,
    "token" : "YOUR_TOKEN",
    "small_batch_url": "https://api.stitchdata.com/v2/import/batch",
    "big_batch_url": "https://api.stitchdata.com/v2/import/batch",
    "batch_size_preferences": {}
}
```

5. Generate the catalog.json file
```
tap-customerx --config tap_config.json --discover > catalog.json
```


## Run
`tap-customerx --config tap_config.json --catalog catalog.json | target-stitch --config target_config.json >> state.json`

## How-to add new streams
1. Create the stream file on tap_customerx/streams/

Example: tap_customerx/streams/sales.py

```
from tap_customerx.stream import CustomerXIterStream


class SalesStream(CustomerXIterStream):
    base_endpoint = 'sales'
    endpoint = 'sales'
    schema = 'sales'
    key_properties = ['id']
    state_field = 'updated_at'
    pagination = True
    limit = 20

    def get_name(self):
        return self.schema

    def update_endpoint(self):
        self.endpoint = "{}?created_at={}&updated_at={}&page={}&max_results={}".format(self.base_endpoint, self.initial_state.strftime('%Y-%m-%d'), self.earliest_state.strftime('%Y-%m-%d'), self.start, self.limit)
```

2. Create the schema file on tap_custoemrx/schemas/

Example: tap_customerx/schemas/sales.json
```
{
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "updated_at": {
      "type": ["null", "string"],
      "format": "date-time"
    },
    "created_at": {
      "type": ["null", "string"],
      "format": "date-time"
    },
    "customer_name": {
      "type": ["null", "string"]
    }
}
```

3. Edit the __init__ file adding the new stream:

tap_customerx/streams/__init__.py

```
  from .clients import ClientsStream
  from .nps import NPSStream
  from .tasks import TasksStream
+ from .sales import SalesStream
  __all__ = [
+   'SalesStream'
    'ClientsStream',
    'NPSStream',
    'TasksStream'
    ]
```

4. Edit the tap file adding the new stream:

tap_customerx/tap.py

```
  from .streams import (ClientsStream)
  from .streams import (NPSStream)
  from .streams import (TasksStream)
+ from .streams import (SalesStream)

  logger = singer.get_logger()

  class CustomerXTap(object):
      streams = [
+         SalesStream(),
          ClientsStream(),
          NPSStream(),
          TasksStream()
      ]

```

5. [Update the catalog.json file](#setup)

---

Copyright &copy; 2019 Jusi
