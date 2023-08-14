from utils.crawlers.crawler import Crawler
from loguru import logger
from datetime import datetime
import constants
import json
from utils import cache


class FetchFromFile:
    def __init__(self, url: str) -> None:
        self.__crawler = Crawler.select_crawler(url)
        url_details = cache.fetch_url_details(url)

        self.url = url
        self.account = self.__crawler.metadata["account"]
        self.ot = url_details["ot"]
        self.plugin_name = url_details["plugin_name"]

    def fetch_crawl_status(self) -> dict:
        crawl_status_file_path = constants.STATUS_PATH(self.ot)
        try:
            with open(crawl_status_file_path, "r") as crawl_status_file:
                all_crawl_status = json.load(crawl_status_file)
                return all_crawl_status[self.plugin_name][self.account]
        except FileNotFoundError:
            logger.warning(
                f"[FETCH ERROR] File {crawl_status_file_path} does not exist. Returning default crawl_status."
            )
        except KeyError:
            logger.warning(
                f"[FETCH ERROR] File {crawl_status_file_path} does not contain key {self.plugin_name}.{self.account}. Returning default crawl_status."
            )
        return constants.DEFAULT_CRAWL_STATUS

    def fetch_metadata(self) -> dict:
        metadata_file_path = constants.METADATA_PATH(
            self.ot, self.plugin_name, self.account
        )
        try:
            with open(metadata_file_path, "r") as metadata_file:
                return json.load(metadata_file)
        except FileNotFoundError:
            logger.warning(f"[FETCH ERROR] File {metadata_file_path} does not exist.")
        return self.__crawler.metadata


class FetchFromURL:
    def __init__(self, url: str) -> None:
        self.crawler = Crawler.select_crawler(url)
        self.url = url

    def __fetch_gh_repo_details_if_required(self):
        if not self.crawler.is_repo_fetched():
            self.crawler.fetch_gh_repo_details()

    def __fetch_gh_issues_details_if_required(self):
        if not self.crawler.is_issues_fetched():
            self.crawler.fetch_gh_issues_details()

    def __fetch_gh_pr_details_if_required(self):
        if not self.crawler.is_pulls_fetched():
            self.crawler.fetch_gh_pr_details()

    def __fetch_readme_if_required(self):
        if not self.crawler.is_readme_fetched():
            self.crawler.fetch_readme()

    def __fetch_sample_config_if_required(self):
        if not self.crawler.is_sample_config_fetched():
            self.crawler.fetch_sample_config()

    def __fetch_last_updated_at(self) -> str:
        self.__fetch_gh_repo_details_if_required()
        self.crawler.extract_metadata()
        return self.crawler.metadata["timestamps"]["ts_last_updated_at"]

    def is_fetch_required(self, prev_crawl_status: dict) -> bool:
        return prev_crawl_status["ts_fetched_at"] < self.__fetch_last_updated_at()

    def fetch_crawl_status(self) -> dict:
        _ts = datetime.utcnow().strftime(constants.TIMESTAMP_FORMAT)
        return {
            "ts_status_verified_at": _ts,
            "ts_fetched_at": _ts,
            "status": "OK",
        }

    def fetch_metadata(self) -> dict:
        self.__fetch_gh_repo_details_if_required()
        self.__fetch_gh_issues_details_if_required()
        self.__fetch_gh_pr_details_if_required()
        self.crawler.extract_metadata()
        return self.crawler.metadata

    def fetch_readme(self) -> bytes:
        self.__fetch_readme_if_required()
        return self.crawler.readme_contents

    def fetch_config_options(self) -> list:
        self.__fetch_sample_config_if_required()
        self.__fetch_readme_if_required()
        self.crawler.extract_config_options()
        return self.crawler.config_options
