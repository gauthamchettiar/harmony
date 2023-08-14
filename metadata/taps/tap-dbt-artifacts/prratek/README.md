# tap-dbt-artifacts
[![test](https://github.com/prratek/tap-dbt-artifacts/actions/workflows/test.yml/badge.svg)](https://github.com/prratek/tap-dbt-artifacts/actions/workflows/test.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI Version](https://img.shields.io/pypi/v/tap-dbt-artifacts?style=flat)](https://pypi.org/project/tap-dbt-artifacts/)
[![License](https://img.shields.io/pypi/l/tap-dbt-artifacts)](LICENSE.md)
[![Python](https://img.shields.io/pypi/pyversions/tap-dbt-artifacts)](https://pypi.org/project/tap-dbt-artifacts/)

`tap-dbt-artifacts` is a Singer Tap for artifacts [generated](https://docs.getdbt.com/reference/artifacts/dbt-artifacts) 
by running dbt commands built with the Meltano [SDK](https://gitlab.com/meltano/singer-sdk) for Singer Taps. 

:warning: It currently supports the v1 schemas introduced in `dbt==0.18.1` for each of the 4 main artifacts listed below 
and is **not compatible with artifacts generated by versions of dbt older than 0.18.1** :warning:

| Artifact | File Name | Description |
| -------- | --------- | ----------- |
| Manifest | manifest.json | Representation of all resources in your dbt project |
| Run Results | run_results.json | Info about the last completed dbt invocation |
| Catalog | catalog.json | Info about tables and views produced in your warehouse by dbt |
| Sources | sources.json | Info about source freshness checks |

## Installation

The easiest way to run this tap is with [Meltano](https://meltano.com/docs/) - you can install it in your Meltano 
project as a "custom extractor" (full instructions [here](https://meltano.com/docs/getting-started.html#add-an-extractor-to-pull-data-from-a-source))
```bash
meltano add --custom extractor tap-dbt-artifacts
```

Alternatively, to use this tap in a Singer pipeline without Meltano you can install it using [pipx](https://pypa.github.io/pipx/comparisons/#pipx-vs-pip)
```bash
pipx install tap-dbt-artifacts
```
or pip
```bash
pip install tap-dbt-artifacts
```

## Configuration

### Accepted Config Options

This tap takes only a single config option `dbt_target_dir`, the full path to your dbt target directory. A full list of 
supported settings and capabilities for this tap is also available by running:
```bash
tap-dbt-artifacts --about
```

You can configure the tap when using Meltano using
```bash
meltano config tap-dbt-artifacts set dbt_target_dir '/path/to/dbt/target'
```

### Source Authentication and Authorization

Note that since the tap is simply loading a local file to a Singer Target of your choice, it does not require any
authentication.

## Usage

You can easily run `tap-dbt-artifacts` by itself or in a pipeline using [Meltano](www.meltano.com).

### Executing the Tap Directly

```bash
tap-dbt-artifacts --version
tap-dbt-artifacts --help
tap-dbt-artifacts --config CONFIG --discover > ./catalog.json
```

### Executing with Meltano

```bash
meltano elt tap-dbt-artifacts <loader> --job_id=<pipeline-name>
```

## Developer Resources


### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_dbt_artifacts/tests` subfolder and then run:

```bash
poetry run pytest
```

You can also test the `tap-dbt-artifacts` CLI interface directly using `poetry run`:

```bash
poetry run tap-dbt-artifacts --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

This project comes with a custom `meltano.yml` project file already created. Install Meltano (if you haven't already) 
and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-dbt-artifacts
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-dbt-artifacts --version
# OR run a test `elt` pipeline:
meltano elt tap-dbt-artifacts target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://gitlab.com/meltano/singer-sdk/-/blob/main/docs/dev_guide.md) for more instructions on how 
to use the SDK to develop your own taps and targets.

### To Do

1. Include meltano.yml file with project to simplify testing for local dev
2. Support config option for dbt schema version
3. Write tests to ensure top level keys for each stream are correct