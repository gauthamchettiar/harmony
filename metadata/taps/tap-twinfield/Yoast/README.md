# tap-twinfield

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from [Twinfield](https://accounting2.twinfield.com/webservices/documentation/#/ApiReference/Request/BrowseData)
- Extracts the following resources:
  - 000 - General Ledger Transactions
  - 010 - Transactions still to be matched
  - 020 - Transaction List
  - 030_3 - General Ledger Details
  - 040_1 - Annual Report (Totals)
  - 060 - Annual Report (Totals Multicurrency)
  - 230_2 - Suppliers (v2)
  - 410 - Bank Transactions
  - 670 - Transaction Summary
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

### Step 1: Create an user

This user needs to have access to the reports.

### Step 2: Configure

Create a file called `twinfield_config.json` in your working directory, following [sample_config.json](sample_config.json). The required parameters are the `username`, `password`, `organisation` and `office`.

This requires a `state.json` file to let the tap know from when to retrieve data. For example:
```
{
    "bookmarks": {
      "bank_transactions": {
        "start_date": "2021-01"
      },
      "general_ledger_details": {
        "start_date": "2021-01"
      }
    }
}
```
Will replicate bank transactions and general ledger details data from 2021-01-01.

### Step 3: Install and Run

Create a virtual Python environment for this tap. This tap has been tested with Python 3.7, 3.8 and 3.9 and might run on future versions without problems.
```
python -m venv singer-twinfield
singer-twinfield/bin/python -m pip install --upgrade pip
singer-twinfield/bin/pip install git+https://github.com/Yoast/singer-tap-twinfield.git
```

This tap can be tested by piping the data to a local JSON target. For example:

Create a virtual Python environment with `singer-json`
```
python -m venv singer-json
singer-json/bin/python -m pip install --upgrade pip
singer-json/bin/pip install target-json
```

Test the tap:

```
singer-twinfield/bin/tap-twinfield --state state.json -c twinfield_config.json | singer-json/bin/target-json >> state_result.json
```

Copyright &copy; 2021 Yoast