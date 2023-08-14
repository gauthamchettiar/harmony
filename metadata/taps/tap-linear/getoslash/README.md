# tap-linear

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

## Installation

See the getting-started guide:

https://github.com/singer-io/getting-started

## Usage

This section dives into basic usage of `tap-linear` by walking through extracting
data from the api.

### Create the configuration file

Create a config file containing the linear credentials, e.g.:

```json
{
  "auth_token": "your-auth-token",
  "start_date": "2017-01-01T00:00:00Z"
}
```

### Discovery mode

The tap can be invoked in discovery mode to find the available linear entities.

```bash
$ tap-linear --config config.json --discover

```

A discovered catalog is output, with a JSON-schema description of each table. A
source table directly corresponds to a Singer stream.

### Field selection

In sync mode, `tap-linear` consumes the catalog and looks for streams that have been
marked as _selected_ in their associated metadata entries.

Redirect output from the tap's discovery mode to a file so that it can be
modified:

```bash
$ tap-linear --config config.json --discover > catalog.json
```

Then edit `catalog.json` to make selections. The stream's metadata entry (associated
with `"breadcrumb": []`) gets a top-level `selected` flag, as does its columns' metadata
entries.

```diff
[
  {
    "breadcrumb": [],
    "metadata": {
      "valid-replication-keys": [
        "updatedAt"
      ],
      "table-key-properties": [
        "id"
      ],
      "forced-replication-method": "INCREMENTAL",
+      "selected": "true"
    }
  },
]
```

### Sync mode

With a `catalog.json` that describes field and table selections, the tap can be invoked in sync mode:

```bash
$ tap-linear --config config.json --catalog catalog.json
```

Issues are written to standard output following the Singer specification. The
resultant stream of JSON data can be consumed by a Singer target.
