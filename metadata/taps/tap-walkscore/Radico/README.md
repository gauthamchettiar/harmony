# tap-walkscore

Singer tap to extract data from the WalkScore API, conforming to the Singer
spec: https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md

WalkScore API: https://www.walkscore.com/professional/api.php

## Setup

`python3 setup.py install`

## Running the tap

#### Discover mode:

`tap-walkscore --config config.json --discover > catalog.json`

#### Sync mode:

`tap-walkscore --config config.json -p catalog.json`