# tap-gleantap

Singer tap to extract data from the GleanTap API, conforming to the Singer
spec: https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md

GleanTap API: https://app.gleantap.com/docs/

## Setup

`python3 setup.py install`

## Running the tap

#### Discover mode:

`tap-gleantap --config config.json --discover > catalog.json`

#### Sync mode:

`tap-gleantap --config config.json -p catalog.json`