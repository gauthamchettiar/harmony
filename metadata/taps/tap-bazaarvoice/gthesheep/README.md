# tap-bazaarvoice

`tap-bazaarvoice` is a Singer tap for the [Bazaarvoice API](https://developer.bazaarvoice.com/conversations-api/reference/v5.4).

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

```bash
pipx install git+https://github.com/gthesheep/tap-bazaarvoice.git
```

## Configuration

### Accepted Config Options

* api_key: API Token gained from Bazaarvoice
* environment: Bazaarvoice environment (staging/ production)
* api_version: API Version, i.e. "5.4"
* page_size: Page size for pagination, default 10

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-bazaarvoice --about
```

### Source Authentication and Authorization

Obtaining API Keys can be done via the process described [here](https://developer.bazaarvoice.com/conversations-api/api-key-processes/requesting-api-keys).

## Usage

You can easily run `tap-bazaarvoice` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-bazaarvoice --version
tap-bazaarvoice --help
tap-bazaarvoice --config CONFIG --discover > ./catalog.json
```

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_bazaarvoice/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-bazaarvoice` CLI interface directly using `poetry run`:

```bash
poetry run tap-bazaarvoice --help
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
cd tap-bazaarvoice
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-bazaarvoice --version
# OR run a test `elt` pipeline:
meltano elt tap-bazaarvoice target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
