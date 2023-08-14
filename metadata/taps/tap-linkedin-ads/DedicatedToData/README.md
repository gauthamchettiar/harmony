# tap-linkedin-marketing

Singer tap to extract data from the LinkedIn Marketing API, conforming to the Singer
spec: https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md

LinkedIn Ad Reporting API: https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/ads-reporting

## Setup

`python3 setup.py install`

## Running the tap

#### Discover mode:

`tap-linkedin-marketing --config config.json --discover > catalog.json`

#### Sync mode:

`tap-linkedin-marketing --config config.json -p catalog.json`