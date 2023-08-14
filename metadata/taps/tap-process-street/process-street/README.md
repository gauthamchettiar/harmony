# tap-process-street

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from [Process Street](http://process.st)
- API documentation [here](https://developer.process.st/)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state
- Supports stream selection but not field selection

## Background

Read the Singer Getting Started guide [here](https://github.com/singer-io/getting-started).

## Quick Start

Ensure you have Python3, Pip & Virtual Envs installed.  A guide is available 
[here](https://github.com/singer-io/getting-started/blob/master/docs/RUNNING_AND_DEVELOPING.md#running-singer-with-python)

1. Setup virtual environment and install

    ```
    python3 -m venv ~/.virtualenvs/tap-process-street
    source ~/.virtualenvs/tap-process-street/bin/activate
    pip install -e .
    ```

2. Create the config file

   Create a JSON file called `config.json` based on the `sample-config.json`

   See the Singer docs on config file
   [here](https://github.com/singer-io/getting-started/blob/master/docs/CONFIG_AND_STATE.md#config-file).

4. Run the Tap in Discovery Mode
    ```
    tap-process-street -c config.json --discover > catalog.json
    ```
   
   See the Singer docs on discovery mode
   [here](https://github.com/singer-io/getting-started/blob/master/docs/DISCOVERY_MODE.md#discovery-mode).

5. Update the catalog.json to include the data you want to include in the sync.

   To select a stream add `"selected": "true"` to it's root `"breadcrumb": []` metadata section in the catalog 
    ```
    {
      "breadcrumb": [],
      "metadata": {
        "selected": "true",
        ...
      }
    }
    ```
 
   See the Singer docs for more advanced stream selection
   [here](https://github.com/singer-io/getting-started/blob/master/docs/SYNC_MODE.md#streamfield-selection) 

5. Run the Tap in Sync Mode
    ```
   tap-process-street -c config.json --catalog catalog.json
    ```
   
Copyright &copy; 2020 Process Street
