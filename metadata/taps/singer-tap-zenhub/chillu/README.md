# tap-zenhub

## Overview

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from [Zenhub](http://zenhub.com)
- Extracts the following resources:
  - [Issues](https://github.com/ZenHubIO/API#get-issue-data)
  - [Issue Events](https://github.com/ZenHubIO/API#get-issue-events)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

Due to limitations in the Zenhub API, issue events are pulled for all
existing issues - there is no way to tell when an issue was last updated with Zenhub.


## Quick start

1. Install through [pipenv](https://pipenv.org/)

    ```
    pipenv install git+https://github.com/chillu/singer-tap-zenhub.git@master#egg=tap_zenhub
    ```

2. Create a GitHub access token

    Login to your GitHub account, go to the
    [Personal Access Tokens](https://github.com/settings/tokens) settings
    page, and generate a new token with at least the `repo` scope. Save this
    access token, you'll need it for the next step.

3. Create a [Zenhub API token](https://github.com/ZenHubIO/API).

4. Create the config file

    Create a JSON file containing the access token you just created
    and the path to the repository. The repo paths are relative to
    `https://github.com/`. For example the path for this repository is
    `singer-io/tap-github`.

    ```json
    {
        "github_token": "",
        "zenhub_token": "",
        "repos": [
            "some-org/some-repo",
            "some-org/some-other-repo"
        ]
    }
    ```


4. Run the application

    ```bash
    pipenv run tap-zenhub --config config.json --state state.json
    ```

5. Using state

Supplying a `state.json` helps the tap to reduce API calls,
and only fetch closed issues since the last run.
It will also re-start partial imports on a repo,
and prioritise repos with the least recent import runs.

First you'll need to create an empty state file:

```
echo '{"bookmarks": {"issues": {}}}' > state.json
```

Now you can run it with that empty state:

```
pipenv run tap-zenhub --config config.json --state state.json
```

In order to write new state, you'll need to send to a target.
Here's an example with the [Stitch Target](https://github.com/singer-io/target-stitch).

```
pipenv run tap-zenhub --state state.json --config config.json | target-stitch --config target-config.json -v  > state.tmp.json && rm state.json && mv state.tmp.json state.json
```

## Development

Install as an [editable dependency](https://docs.pipenv.org/basics/#editable-dependencies-e-g-e)

```bash
git clone https://github.com/chillu/singer-tap-zenhub.git
pipenv install --dev -e .
```