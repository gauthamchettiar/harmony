# tap-mindstamp

`tap-mindstamp` is a Singer tap for Mindstamp.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation
```bash
pipx install tap-mindstamp
```

## Configuration

### Accepted Config Options
A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-mindstamp --about
```

## Usage

You can easily run `tap-mindstamp` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-mindstamp --version
tap-mindstamp --help
tap-mindstamp --config CONFIG --discover > ./catalog.json
```

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_mindstamp/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-mindstamp` CLI interface directly using `poetry run`:

```bash
poetry run tap-mindstamp --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created.
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-mindstamp
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-mindstamp --version
# OR run a test `elt` pipeline:
meltano elt tap-mindstamp target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
