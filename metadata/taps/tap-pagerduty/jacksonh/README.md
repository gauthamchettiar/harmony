# tap-pagerduty

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap pulls raw incident data from the [PagerDuty REST API](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Incidents/get_incidents) and extracts the
following fields:

- id
- status
- summary
- html_url
- last_status_change_by/summary
- created_at
- last_status_change_at'


## Quick Start

1. Create the config file

   Create a JSON file called `config.json`. Its contents should look like:

   ```json
    {
        "start_date": "2010-01-01",
        "api_key": "<PagerDuty API Key>"
    }
    ```

   The `start_date` specifies the date at which the tap will begin pulling data
   (for those resources that support this).

   The `api_key` is a `v2 Current` read-only API key from PagerDuty you can
   create a PagerDuty API key here: https://juvomobile.pagerduty.com/api_keys

2. Run the Tap in Discovery Mode

    tap-pagerduty -c config.json -d

   See the Singer docs on discovery mode
   [here](https://github.com/singer-io/getting-started/blob/master/BEST_PRACTICES.md#discover-mode-and-connection-checks).

3. Run the Tap in Sync Mode

    tap-pagerduty -c config.json