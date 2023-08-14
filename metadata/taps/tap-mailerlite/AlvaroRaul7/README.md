# tap-mailerlite

`tap-mailerlite` is a Singer tap for mailerlite.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

<!--

Developer TODO: Update the below as needed to correctly describe the install procedure. For instance, if you do not have a PyPi repo, or if you want users to directly install from your git repo, you can modify this step as appropriate.

## Installation

Install from PyPi:

```bash
pipx install tap-mailerlite
```

Install from GitHub:

```bash
pipx install git+https://github.com/ORG_NAME/tap-mailerlite.git@main
```

-->

## Configuration

### Accepted Config Options

<!--
Developer TODO: Provide a list of config options accepted by the tap.

This section can be created by copy-pasting the CLI output from:

```
tap-mailerlite --about --format=markdown
```
-->

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-mailerlite --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

<!--
Developer TODO: If your tap requires special access on the source system, or any special authentication requirements, provide those here.
-->

## Usage

You can easily run `tap-mailerlite` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-mailerlite --version
tap-mailerlite --help
tap-mailerlite --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.



### Install Singer Discover in your local environment

```bash
pip install https://github.com/chrisgoddard/singer-discover/archive/master.zip
```

### Initialize your Development Environment for the Tap

```bash
source venv/bin/activate
pip install poetry
poetry install
```

### Initialize your Development Environment for the Target

```bash
python3 -m venv ~/.virtualenvs/target-csv
source ~/.virtualenvs/target-csv/bin/activate
pip install target-csv
```
### Create and Run Tests

Create tests within the `tap_mailerlite/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-mailerlite` CLI interface directly using `poetry run`:

```bash
poetry run tap-mailerlite --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

<!--
Developer TODO:
Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any "TODO" items listed in
the file.
-->

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-mailerlite
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-mailerlite --version
# OR run a test `elt` pipeline:
meltano elt tap-mailerlite target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
