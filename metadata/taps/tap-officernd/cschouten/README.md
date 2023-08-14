# tap-officernd

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from [Officernd](https://officernd.com)
- Extracts the following resources:
  - [bookings](https://developer.officernd.com/#bookings)
  - [charges](https://developer.officernd.com/#charges)
  - [checkins](https://developer.officernd.com/#checkins)
  - [credits](https://developer.officernd.com/#credits)
  - [events](https://developer.officernd.com/#events)
  - [fees](https://developer.officernd.com/#fees)
  - [floors](https://developer.officernd.com/#floors)
  - [members](https://developer.officernd.com/#members)
  - [memberships](https://developer.officernd.com/#memberships)
  - [offices](https://developer.officernd.com/#offices)
  - [payments](https://developer.officernd.com/#payments)
  - [plans](https://developer.officernd.com/#plans)
  - [posts](https://developer.officernd.com/#posts)
  - [resource_types](https://developer.officernd.com/#resource-types)
  - [resources](https://developer.officernd.com/#resources)
  - [teams](https://developer.officernd.com/#teams)
  - [visits](https://developer.officernd.com/#visits)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

##Quick Start

Note: Because this tap isn't yet available publicly, you'll need to create a virtual environment.

1. Download `tap-officernd` repo to local machine
2. Run the following commands:
   ```
   cd tap-officernd 
   python3 -m venv ~/.virtualenvs/tap-officernd
   source ~/.virtualenvs/tap-officernd/bin/activate
   ```
3. Install the package:
   ```
   pip install -e .
   ```

4. Edit and rename `sample_config.json`. Be sure to enter your client id, client secret, organization name, 
   and any custom fields. Custom fields should be formatted as follows:
   ```
   {...
   "custom_fields": {"[NAME OF FIELD]": "[module]",...
   }
   ```

5. Invoke the tap in discovery mode to get the catalog:
   ```
   tap-officernd -c sample_config.json --discover
   ```
   The output should be a catalog file with the single sample stream (from the schemas folder).


6. If this catalog is saved to a catalog.json file, it can be passed back into the tap in sync mode:
   ```
   tap-officernd -c sample_config.json --properties catalog.json
   ```
---

Copyright &copy; 2018 Stitch
