# tap-partoo
`tap-partoo` is a Singer tap for the [Partoo REST API](https://developers.partoo.co/).

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation
You can install the Singer tap with:

```bash
pipx install git+https://github.com/GendarmerieNationale/tap-partoo.git
```

## Configuration

| Setting    | Required | Default | Description                       |
|:-----------|:--------:|:-------:|:----------------------------------|
| api_key    |   True   |  None   | Partoo API Key                    |
| start_date |   True   |  None   | Start syncing data from that date |

A full list of supported settings and capabilities is available by running: `tap-partoo --about`

## Usage

You can easily run `tap-partoo` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-partoo --version
tap-partoo --help
tap-partoo --config path/to/config.json --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

After cloning the repo locally, inside the repo:
```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_partoo/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-partoo` CLI interface directly using `poetry run`:

```bash
poetry run tap-partoo --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-partoo
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-partoo --version
# OR run a test `elt` pipeline:
meltano elt tap-partoo target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.


## Contact
Gendarmerie Nationale, cyberimpact@gendarmerie.interieur.gouv.fr

This was developed as part of the [CyberImpact EIG project](https://eig.etalab.gouv.fr/defis/cyberimp-ct/).
