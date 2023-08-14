import constants
import json
import os


class URLNotProvidedInRepository(Exception):
    def __init__(self) -> None:
        message = "[URL NOT PRESENT IN repositories.json] Add the URL."
        super().__init__(message)


def cache_url_details():
    tap_repository_file_path = constants.REPOSITORY_PATH(constants.ObjectType.TAP)
    target_repository_file_path = constants.REPOSITORY_PATH(constants.ObjectType.TARGET)
    url_path = constants.URL_PATH

    with open(tap_repository_file_path, "r") as tap_repo_file, open(
        target_repository_file_path, "r"
    ) as target_repo_file:
        url_dict = {}
        tap: dict = json.load(tap_repo_file)
        target: dict = json.load(target_repo_file)

        for plugin_name, repositories in tap.items():
            for url in repositories:
                url_dict[url] = {
                    "ot": constants.ObjectType.TAP.value,
                    "plugin_name": plugin_name,
                }

        for plugin_name, repositories in target.items():
            for url in repositories:
                url_dict[url] = {
                    "ot": constants.ObjectType.TARGET.value,
                    "plugin_name": plugin_name,
                }
    os.makedirs(os.path.dirname(url_path), exist_ok=True)
    with open(url_path, "w+") as url_file:
        json.dump(url_dict, url_file)


def fetch_url_details(url: str, refresh_cache: bool = False):
    url_path = constants.URL_PATH

    if refresh_cache or not os.path.exists(url_path):
        cache_url_details()
    try:
        with open(url_path, "r") as url_file:
            url_dict = json.load(url_file)
        if url not in url_dict:
            return fetch_url_details(url, refresh_cache=True)
        return url_dict[url]
    except KeyError:
        raise URLNotProvidedInRepository()
