# tap-typeform

`tap-typeform` is a Singer tap for Typeform.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

```bash
pipx install git+https://github.com/albert-marrero/tap-typeform
```

## Configuration
A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-typeform --about
```

### Capabilities

* `sync`
* `catalog`
* `state`
* `discover`

### Source Authentication and Authorization

You will need to [create a personal access token for Typeform's API.](https://developer.typeform.com/get-started/personal-access-token/)

### Configuration
```json
{
    "personal_access_token": "ACCESS_TOKEN",
}
```
A bit of a run down on each of the properties:
- **personal_access_token**: Your personal access token for Typeform's API.

## Usage

You can easily run `tap-typeform` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-typeform --version
tap-typeform --help
tap-typeform --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_typeform/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-typeform` CLI interface directly using `poetry run`:

```bash
poetry run tap-typeform --help
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
cd tap-typeform
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-typeform --version
# OR run a test `elt` pipeline:
meltano elt tap-typeform target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.

## Contributing
For major changes, please open an issue first to discuss what you would like to change.

## Support
If you enjoy this repository, please [star](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars) this repository. By starring a repository, it shows appreciation to the repository maintainer for their work. Many of GitHub's repository rankings depend on the number of stars a repository has.

## License
[MIT](LICENSE)