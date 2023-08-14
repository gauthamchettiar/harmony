import constants
import json
from utils import dump, fetch
from datetime import datetime
from utils.crawlers.github import InvalidGithubRepoLinkException
from loguru import logger


class RunSync:
    @staticmethod
    def __sync(repository_path: str):
        with open(repository_path, "r") as repository_file:
            repository_dict: dict = json.load(repository_file)

        for _, repositories in repository_dict.items():
            try:
                for repository_url in repositories:
                    fff = fetch.FetchFromFile(repository_url)
                    ffu = fetch.FetchFromURL(repository_url)
                    dtf = dump.DumpToFile(repository_url)
                    prev_crawl_status = fff.fetch_crawl_status()

                    if ffu.is_fetch_required(prev_crawl_status):
                        dtf.dump_readme(ffu.fetch_readme())
                        dtf.dump_config_options(ffu.fetch_config_options())
                        dtf.dump_metadata(ffu.fetch_metadata())
                        dtf.dump_crawl_status(ffu.fetch_crawl_status())
            except InvalidGithubRepoLinkException:
                logger.warning(
                    f"[{repository_url}] Got non github.com link, will skip processing"
                )

    @staticmethod
    def sync_taps():
        tap_repository_path = constants.REPOSITORY_PATH(constants.ObjectType.TAP)
        RunSync.__sync(tap_repository_path)

    @staticmethod
    def sync_targets():
        target_repository_path = constants.REPOSITORY_PATH(constants.ObjectType.TARGET)
        RunSync.__sync(target_repository_path)
