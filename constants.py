# fmt: off
from enum import Enum
from os.path import join
from typing import Any

# enums
class ObjectType(Enum):
    TAP = "tap"
    TARGET = "target"


# folder/file/placeholder names
METADATA_FOLDER_NAME = "metadata"
TAPS_FOLDER_NAME = "taps"
TARGETS_FOLDER_NAME = "targets"
REPOSITORY_FILE_NAME = "repositories.json"
STATUS_FILE_NAME = "crawl_status.json"
METADATA_FILE_NAME = "metadata.json"
CONFIG_OPTIONS_FILE_NAME = "config_options.json"
README_FILE_NAME = "README.md"
URL_FILE_NAME = ".cache/urls.json"
PLUGIN_NAME_PLACEHOLDER = "{plugin_name}"
ACCOUNT_PLACEHOLDER = "{account}"

# folder/file paths
TAPS_PATH = join(METADATA_FOLDER_NAME, TAPS_FOLDER_NAME)  # metadata/taps
TARGETS_PATH = join(METADATA_FOLDER_NAME, TARGETS_FOLDER_NAME)  # metadata/targets
TAPS_REPOSITORY_PATH = join(TAPS_PATH, REPOSITORY_FILE_NAME)  # metadata/taps/repositories.json
TARGETS_REPOSITORY_PATH = join(TARGETS_PATH, REPOSITORY_FILE_NAME)  # metadata/targets/repositories.json
TAPS_STATUS_PATH = join(TAPS_PATH, STATUS_FILE_NAME)  # metadata/taps/status.json
TARGETS_STATUS_PATH = join(TARGETS_PATH, STATUS_FILE_NAME)  # metadata/targets/status.json
TAPS_METADATA_PATH = join(TAPS_PATH, PLUGIN_NAME_PLACEHOLDER , ACCOUNT_PLACEHOLDER, METADATA_FILE_NAME)  # metadata/taps/{plugin_name}/{account}/metadata.json
TARGETS_METADATA_PATH = join(TARGETS_PATH, PLUGIN_NAME_PLACEHOLDER , ACCOUNT_PLACEHOLDER, METADATA_FILE_NAME)  # metadata/targets/{plugin_name}/{account}/metadata.json
TAPS_CONFIG_OPTIONS_PATH = join(TAPS_PATH, PLUGIN_NAME_PLACEHOLDER , ACCOUNT_PLACEHOLDER, CONFIG_OPTIONS_FILE_NAME)  # metadata/taps/{plugin_name}/{account}/config_options.json
TARGETS_CONFIG_OPTIONS_PATH = join(TARGETS_PATH, PLUGIN_NAME_PLACEHOLDER , ACCOUNT_PLACEHOLDER, CONFIG_OPTIONS_FILE_NAME)  # metadata/targets/{plugin_name}/{account}/config_options.json
TAPS_README_PATH = join(TAPS_PATH, PLUGIN_NAME_PLACEHOLDER , ACCOUNT_PLACEHOLDER, README_FILE_NAME)  # metadata/taps/{plugin_name}/{account}/README.md
TARGETS_README_PATH = join(TARGETS_PATH, PLUGIN_NAME_PLACEHOLDER , ACCOUNT_PLACEHOLDER, README_FILE_NAME)  # metadata/targets/{plugin_name}/{account}/README.md
URL_PATH = join(METADATA_FOLDER_NAME, URL_FILE_NAME)

# generic paths
def BASE_PATH(ot: ObjectType) -> str:
    if ot == ObjectType.TAP or ot == ObjectType.TAP.value:
        return TAPS_PATH
    return TARGETS_PATH

def REPOSITORY_PATH(ot: ObjectType|str) -> str:
    if ot == ObjectType.TAP or ot == ObjectType.TAP.value:
        return TAPS_REPOSITORY_PATH
    return TARGETS_REPOSITORY_PATH

def STATUS_PATH(ot: ObjectType|str) -> str:
    if ot == ObjectType.TAP or ot == ObjectType.TAP.value:
        return TAPS_STATUS_PATH
    return TARGETS_STATUS_PATH

def METADATA_PATH(ot: ObjectType|str, plugin_name:str, account:str) -> str:
    if ot == ObjectType.TAP or ot == ObjectType.TAP.value:
        return TAPS_METADATA_PATH.format(plugin_name=plugin_name, account=account)
    return TARGETS_METADATA_PATH.format(plugin_name=plugin_name, account=account)

def CONFIG_OPTIONS_PATH(ot: ObjectType|str, plugin_name:str, account:str) -> str:
    if ot == ObjectType.TAP or ot == ObjectType.TAP.value:
        return TAPS_CONFIG_OPTIONS_PATH.format(plugin_name=plugin_name, account=account)
    return TARGETS_CONFIG_OPTIONS_PATH.format(plugin_name=plugin_name, account=account)

def README_PATH(ot: ObjectType|str, plugin_name:str, account:str) -> str:
    if ot == ObjectType.TAP or ot == ObjectType.TAP.value:
        return TAPS_README_PATH.format(plugin_name=plugin_name, account=account)
    return TARGETS_README_PATH.format(plugin_name=plugin_name, account=account)


# others
TIMESTAMP_FORMAT: str = "%Y-%m-%dT%H:%M:%S%ZZ"
DEFAULT_CRAWL_STATUS: dict[str,Any] = {
    "ts_status_verified_at": "1970-01-01T00:00:00Z",
    "ts_fetched_at": "1970-01-01T00:00:00Z",
    "status": "STALE",
}
DEFAULT_METADATA: dict[str,Any]= {
    "url": None,
    "api_url": None,
    "account": None,
    "repo_name": None,
    "account_type": None,
    "language": None,
    "readme": {
        "is_present": None,
        "url": None
    },
    "sample_config": {
        "is_present": None,
        "url": None
    },
    "stats": {
        "num_stars": None,
        "num_watchers": None,
        "num_forks": None,
        "num_networks": None,
        "num_subscribers": None,
        "num_open_issues": None,
        "num_open_issues_30D": None,
        "num_closed_issues": None,
        "num_closed_issues_30D": None,
        "num_open_pr": None,
        "num_open_pr_30D": None,
        "num_closed_pr": None,
        "num_closed_pr_30D": None,
    },
    "timestamps": {
        "ts_created_at": None,
        "ts_last_updated_at": None,
        "ts_last_pushed_at": None,
        "ts_last_open_issue_at": None,
        "ts_last_closed_issue_at": None,
        "ts_last_open_pr_at": None,
        "ts_last_closed_pr_at": None,
    },
}
REMOTE_README_NAMES = ["README.md", "README.rst"]
REMOTE_SAMPLE_CONFIG_NAMES = ["config.sample.json", "sample_config.json.example", "config.example.json"]
