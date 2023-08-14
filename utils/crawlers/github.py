from datetime import date, timedelta
import json
from typing import Any
from loguru import logger as logger
import os
import requests
from requests import Response
import pytablereader as ptr  # type: ignore
import constants

if os.environ.get("GITHUB_AUTH_TOKEN", None) is None:
    logger.warning(
        "'GITHUB_AUTH_TOKEN' environment variable is required for higher rate limits."
    )


class InvalidGithubRepoLinkException(Exception):
    def __init__(self, link: str) -> None:
        self.message = (
            f"[INVALID GITHUB LINK] '{link}' is not a valid github.com repo link."
        )
        super().__init__(self.message)


class InvalidResponseException(Exception):
    def __init__(self, link: str, status_code: int, content: str) -> None:
        logger.error(f"'{link}' -> ({status_code}) : {content}")
        self.message = (
            f"[INVALID GITHUB LINK] '{link}' is not a valid github.com repo link."
        )
        super().__init__(self.message)


class Github:
    def __init__(self, repo_url: str) -> None:
        self.repo_url: str = repo_url
        if not self.__is_github_link():
            raise InvalidGithubRepoLinkException(repo_url)
        try:
            self.account, self.repo_name = (
                repo_url.split("/")[-2],
                repo_url.split("/")[-1],
            )
            self.GITHUB_AUTH_TOKEN: str | None = os.environ.get(
                "GITHUB_AUTH_TOKEN", None
            )
        except IndexError:
            raise InvalidGithubRepoLinkException(repo_url)
        else:
            self.api_url = (
                f"https://api.github.com/repos/{self.account}/{self.repo_name}"
            )
            self.raw_url = f"https://raw.githubusercontent.com/{self.account}/{self.repo_name}/master"
            self.__fetched: dict = {
                "repo": None,
                "pulls": None,
                "issues": None,
                "readme": None,
                "sample_config": None,
            }
            self.metadata = dict(
                constants.DEFAULT_METADATA,
                **{
                    "url": self.repo_url,
                    "api_url": self.api_url,
                    "account": self.account,
                    "repo_name": self.repo_name,
                },
            )

            self.config_options: list = []

    @property
    def readme_contents(self) -> bytes:
        return self.__fetched["readme"]

    def __is_gh_auth_provided(self) -> bool:
        return self.GITHUB_AUTH_TOKEN != None

    def __is_github_link(self) -> bool:
        return "github.com" in self.repo_url

    def __prepare_headers(self) -> dict[str, str]:
        if self.__is_gh_auth_provided():
            return {
                "Authorization": f"BEARER {self.GITHUB_AUTH_TOKEN}",
                "X-GitHub-Api-Version": "2022-11-28",
            }
        return {}

    def __make_api_call(self, api_path: str = "") -> dict[str, Any]:
        url = self.api_url + api_path
        headers = self.__prepare_headers()
        logger.info(f"[CALLING API] -> {url}")
        response = requests.get(f"{url}", headers=headers)
        if response.status_code != 200:
            raise InvalidResponseException(
                url, response.status_code, str(response.content)
            )

        return response.json()

    def __is_response_valid(self, response: Response) -> bool:
        return response.status_code == 200 and str(response.content) != "404: Not Found"

    def __make_multi_page_call(self, api_path: str = "") -> list[Any]:
        url = (
            api_path + "&per_page=100"
            if "?" in api_path
            else api_path + "?per_page=100"
        )
        pages: list = []
        for pg in range(1, 25):
            response = self.__make_api_call(url + f"&page={pg}")
            pages.extend(response)
            if len(response) < 100:
                break
        return pages

    def __filter_items(
        self,
        items: list,
        state: str | None = None,
        created_ts_gte: str | None = None,
        closed_ts_gte: str | None = None,
    ) -> list:
        if state != None:
            items = [item for item in items if item["state"] == state]
        if created_ts_gte != None:
            items = [item for item in items if item["created_at"] >= created_ts_gte]
        if closed_ts_gte != None:
            items = [item for item in items if item["closed_at"] >= closed_ts_gte]
        return items

    def fetch_gh_repo_details(self) -> None:
        self.__fetched["repo"] = self.__make_api_call()

    def fetch_gh_pr_details(self) -> None:
        self.__fetched["pulls"] = self.__make_multi_page_call("/pulls?state=all")

    def fetch_gh_issues_details(self) -> None:
        self.__fetched["issues"] = self.__make_multi_page_call("/issues?state=all")

    def fetch_readme(self) -> None:
        for readme_name in constants.REMOTE_README_NAMES:
            readme_url = f"{self.raw_url}/{readme_name}"
            logger.info(f"[CALLING API] -> {readme_url}")
            response = requests.get(readme_url)
            if self.__is_response_valid(response):
                self.__fetched["readme"] = response.content
                self.metadata["readme"] = {"is_present": True, "url": readme_url}
                break
            else:
                self.metadata["readme"] = {"is_present": False, "url": None}
                logger.warning(
                    f"[README DOES NOT EXIST] File does not exist at {readme_url}"
                )

    def fetch_sample_config(self) -> None:
        for sample_config_name in constants.REMOTE_SAMPLE_CONFIG_NAMES:
            sample_config_url = f"{self.raw_url}/{sample_config_name}"
            logger.info(f"[CALLING API] -> {sample_config_url}")
            response = requests.get(sample_config_url)
            if self.__is_response_valid(response):
                try:
                    self.__fetched["sample_config"] = json.loads(response.content)
                except json.JSONDecodeError:
                    self.__fetched["sample_config"] = response.content
                self.metadata["sample_config"] = {
                    "is_present": True,
                    "url": sample_config_url,
                }
                break
            else:
                self.metadata["sample_config"] = {"is_present": False, "url": None}
                logger.warning(
                    f"[SAMPLE CONFIG DOES NOT EXIST] File does not exist at {sample_config_url}"
                )

    def is_repo_fetched(self):
        return self.__fetched["repo"] is not None

    def is_issues_fetched(self):
        return self.__fetched["issues"] is not None

    def is_pulls_fetched(self):
        return self.__fetched["pulls"] is not None

    def is_readme_fetched(self):
        return self.__fetched["readme"] is not None

    def is_sample_config_fetched(self):
        return self.__fetched["sample_config"] is not None

    def extract_metadata(self) -> None:
        ts_30D = (date.today() - timedelta(days=30)).isoformat()

        if self.is_repo_fetched():
            repo = self.__fetched["repo"]
            self.metadata["account_type"] = (
                "organization" if repo.get("organization", None) is not None else "user"
            )
            self.metadata["language"] = repo.get("language", None)
            self.metadata["stats"]["num_stars"] = repo.get("stargazers_count", None)
            self.metadata["stats"]["num_watchers"] = repo.get("watchers_count", None)
            self.metadata["stats"]["num_forks"] = repo.get("forks", None)
            self.metadata["stats"]["num_networks"] = repo.get("network_count", None)
            self.metadata["stats"]["num_subscribers"] = repo.get(
                "subscribers_count", None
            )
            self.metadata["timestamps"]["ts_created_at"] = (
                repo.get("created_at", None),
            )
            self.metadata["timestamps"]["ts_last_updated_at"] = repo.get(
                "updated_at", None
            )
            self.metadata["timestamps"]["ts_last_pushed_at"] = repo.get(
                "pushed_at", None
            )

        if self.is_issues_fetched():
            issues = self.__fetched["issues"]
            self.metadata["stats"]["num_open_issues"] = len(
                self.__filter_items(issues, state="open")
            )
            self.metadata["stats"]["num_open_issues_30D"] = len(
                self.__filter_items(issues, state="open", created_ts_gte=ts_30D)
            )
            self.metadata["stats"]["num_closed_issues"] = len(
                self.__filter_items(issues, state="closed")
            )
            self.metadata["stats"]["num_closed_issues_30D"] = len(
                self.__filter_items(issues, state="closed", closed_ts_gte=ts_30D)
            )
            self.metadata["timestamps"]["ts_last_open_issue_at"] = (
                None
                if self.metadata["stats"]["num_open_issues"] == 0
                else self.__filter_items(issues, state="open")[0]["created_at"]
            )
            self.metadata["timestamps"]["ts_last_closed_issue_at"] = (
                None
                if self.metadata["stats"]["num_closed_issues"] == 0
                else self.__filter_items(issues, state="closed")[0]["closed_at"]
            )

        if self.is_pulls_fetched():
            pulls = self.__fetched["pulls"]
            self.metadata["stats"]["num_open_pr"] = len(
                self.__filter_items(pulls, state="open")
            )
            self.metadata["stats"]["num_open_pr_30D"] = len(
                self.__filter_items(pulls, state="open", created_ts_gte=ts_30D)
            )
            self.metadata["stats"]["num_closed_pr"] = len(
                self.__filter_items(pulls, state="closed")
            )
            self.metadata["stats"]["num_closed_pr_30D"] = len(
                self.__filter_items(pulls, state="closed", closed_ts_gte=ts_30D)
            )
            self.metadata["timestamps"]["ts_last_open_pr_at"] = (
                None
                if self.metadata["stats"]["num_open_pr"] == 0
                else self.__filter_items(pulls, state="open")[0]["created_at"]
            )
            self.metadata["timestamps"]["ts_last_closed_pr_at"] = (
                None
                if self.metadata["stats"]["num_closed_pr"] == 0
                else self.__filter_items(pulls, state="closed")[0]["closed_at"]
            )

    def extract_config_options(self):
        if self.is_sample_config_fetched():
            self.config_options.append(
                {
                    "source": "sample_config",
                    "content": self.__fetched["sample_config"],
                    "instance": 0,
                }
            )
        elif self.is_readme_fetched():
            logger.warning("[SAMPLE CONFIG NOT FETCHED] Looking for Tables in README.")
            readme = self.__fetched["readme"]
            md_loader = ptr.TableTextLoader(readme, format_name="markdown")
            tables = [table for table in md_loader.load()]

            if len(tables) == 0:
                logger.warning(
                    "[README DOES NOT HAVE TABLE] Fetched Readme File does not have any tables."
                )
            elif len(tables) > 1:
                logger.warning(
                    "[README HAS MULTIPLE TABLES] Fetched Readme File has multiple tables, Fetching All."
                )
            else:
                for i, table_data in enumerate(tables):
                    table = list(table_data.as_dict().values())[0]
                    self.config_options.append(
                        {"source": "readme", "content": table, "instance": i}
                    )
