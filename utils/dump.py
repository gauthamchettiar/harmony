import constants
import json
from utils import cache
from utils.crawlers.crawler import Crawler
import os
from loguru import logger


class DumpToFile:
    def __init__(self, url: str) -> None:
        self.__crawler = Crawler.select_crawler(url)
        url_details = cache.fetch_url_details(url)
        self.ot = url_details["ot"]
        self.account = self.__crawler.metadata["account"]
        self.repo_name = self.__crawler.metadata["repo_name"]
        self.plugin_name = url_details["plugin_name"]

    def dump_crawl_status(self, crawl_status: dict):
        crawl_status_file_path = constants.STATUS_PATH(self.ot)
        try:
            with open(crawl_status_file_path, "r") as crawl_status_file:
                all_crawl_status = json.load(crawl_status_file)
        except FileNotFoundError:
            all_crawl_status = {}

        all_crawl_status[self.plugin_name] = (
            {}
            if self.plugin_name not in all_crawl_status
            else all_crawl_status[self.plugin_name]
        )
        all_crawl_status[self.plugin_name][self.account] = crawl_status
        logger.debug(f"Writing Crawl Status to '{crawl_status_file_path}'")
        with open(crawl_status_file_path, "w+") as crawl_status_file:
            json.dump(all_crawl_status, crawl_status_file)

    def dump_metadata(self, metadata: dict):
        metadata_file_path = constants.METADATA_PATH(
            self.ot, self.plugin_name, self.account
        )
        os.makedirs(os.path.dirname(metadata_file_path), exist_ok=True)
        logger.debug(f"Writing Metadata to '{metadata_file_path}'")
        with open(metadata_file_path, "w+") as metadata_file:
            json.dump(metadata, metadata_file)

    def dump_readme(self, readme_contents: bytes):
        readme_file_path = constants.README_PATH(
            self.ot, self.plugin_name, self.account
        )
        os.makedirs(os.path.dirname(readme_file_path), exist_ok=True)
        logger.debug(f"Writing Readme to '{readme_file_path}'")
        with open(readme_file_path, "wb") as readme_file:
            if readme_contents is not None:
                readme_file.write(readme_contents)

    def dump_config_options(self, config_options: list):
        config_options_path = constants.CONFIG_OPTIONS_PATH(
            self.ot, self.plugin_name, self.account
        )
        os.makedirs(os.path.dirname(config_options_path), exist_ok=True)
        logger.debug(f"Writing Config Options to '{config_options_path}'")
        with open(config_options_path, "w+") as metadata_file:
            try:
                json.dump(config_options, metadata_file)
            except TypeError:
                metadata_file.write(str(config_options))
