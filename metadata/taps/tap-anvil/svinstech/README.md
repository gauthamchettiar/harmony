# tap-anvil

*tap-anvil* is a Singer tap for Anvil.

A [Singer tap](https://www.singer.io/#taps) extracts data from any source and write it to a standard stream in a JSON-based format.

[Anvil](https://www.useanvil.com/) is a tool for programmatically filling out PDF forms.

---

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/k-aranke/tap-anvil/Test)
![pre-commit.ci status](https://results.pre-commit.ci/badge/github/k-aranke/tap-anvil/main.svg)
![Codecov](https://img.shields.io/codecov/c/github/k-aranke/tap-anvil)

## Installation

```bash
pipx install git+https://github.com/k-aranke/mode-client.git@latest
```

## Usage

Get your Anvil API key using [these instructions](https://www.useanvil.com/docs/api/getting-started#api-key).
Create a `.env` file to save your Anvil API key.

```dotenv
TAP_ANVIL_API_KEY=<your-api-key>
```

Alternatively, save `TAP_ANVIL_API_KEY` as an environment variable.
Now you can run:

```bash
dotenv run tap-anvil --config=ENV
```

## API

The following objects are currently synced:
1. [Organization](https://www.useanvil.com/docs/api/graphql/reference/#definition-Organization)
2. [Weld](https://www.useanvil.com/docs/api/graphql/reference/#definition-Weld)
3. [Forge](https://www.useanvil.com/docs/api/graphql/reference/#definition-Forge)
4. [WeldData](https://www.useanvil.com/docs/api/graphql/reference/#definition-WeldData)
5. [Submission](https://www.useanvil.com/docs/api/graphql/reference/#definition-Submission)

If you'd like to see another object, please open a [feature request](https://github.com/k-aranke/tap-anvil/issues/new?assignees=&labels=&template=feature_request.md&title=).

## References

* [Anvil GraphQL API](https://www.useanvil.com/docs/api/graphql/reference/)
* [Meltano SDK Developer Guide](https://sdk.meltano.com/en/latest/dev_guide.html)
* [Singer Spec](https://hub.meltano.com/singer/spec/)

## Local Development

### Installation

```bash
pipx install poetry
poetry install
```

### Download Data

```bash
pipx install tap-jsonl
rm -rf output/*.jsonl && dotenv run tap-anvil --config=ENV | target-jsonl -c output/target-jsonl-config.json
```

### Testing

```bash
poetry run pytest --cov=tap_anvil
```

### Creating a new release

*tap-anvil* uses [Commitizen](https://commitizen-tools.github.io/commitizen/bump/) to automatically create GitHub releases with [semantic versioning](https://semver.org/).
In practice, this means that prefacing commits with `feat:` will create a minor release and `fix:` will create a patch release.

*tap-anvil* currently isn't published to PyPI.


### Running a GraphQL query locally

Use the [Anvil Postman collection](https://www.postman.com/useanvil/workspace/anvil/overview).


### Caveat

Previously for `CreatedAt`, `UpdatedAt` and some other date attribute, we have 
```
 "createdAt": {
      "anyOf": [
        {
          "type": "null"
        },
        {
          "format": "date-time",
          "type": "string"
        }
	]
    },
```
this kind of type for them. Because we're using `target-snowflake` downstream of `tap-anvil` to load this data into our datawarehouse in Snowflake and there is a [known issue](https://github.com/transferwise/pipelinewise-target-snowflake/issues/228) in `target-snowflake` that it will skip `anyOf` type attribute. So we just make this a `string` type like below.
```
"type": [
        "null",
        "string"
      ]
```
