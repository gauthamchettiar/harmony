import constants
import json
from utils import dump, fetch
from datetime import datetime
from utils.crawlers.github import InvalidGithubRepoLinkException
from loguru import logger
from textwrap import dedent


class RunSync:
    @staticmethod
    def __sync(repository_path: str):
        logger.info(f"Will start syncing repositories in : {repository_path}")

        stat_object, stat_repo, stat_repo_updated = 0, 0, 0

        with open(repository_path, "r") as repository_file:
            repository_dict: dict = json.load(repository_file)

        for object_name, repositories in repository_dict.items():
            stat_object += 1
            logger.info(f"Syncing for object : {object_name}")
            try:
                for repository_url in repositories:
                    logger.info(f"Syncing for repository : {repository_url}")
                    stat_repo += 1
                    fff = fetch.FetchFromFile(repository_url)
                    ffu = fetch.FetchFromURL(repository_url)
                    dtf = dump.DumpToFile(repository_url)
                    prev_crawl_status = fff.fetch_crawl_status()

                    if ffu.is_fetch_required(prev_crawl_status):
                        logger.debug(f"New data available!")
                        stat_repo_updated += 1
                        if (readme := ffu.fetch_readme()) is not None:
                            dtf.dump_readme(readme)
                        if (config_options := ffu.fetch_config_options()) is not None:
                            dtf.dump_config_options(config_options)
                        dtf.dump_metadata(ffu.fetch_metadata())
                    dtf.dump_crawl_status(ffu.fetch_crawl_status())
                    logger.info(f"Completed Syncing for repository : {repository_url}")
            except InvalidGithubRepoLinkException:
                logger.warning(
                    f"Provided URL '{repository_url}' is not a github.com link. Will skip processing repository."
                )
            logger.info(f"Completed Syncing for object : {object_name}")

        logger.info(f"Completed syncing repositories in : {repository_path}")
        return {
            "stat_object": stat_object,
            "stat_repo": stat_repo,
            "stat_repo_updated": stat_repo_updated,
            "stat_repo_skipped": stat_repo - stat_repo_updated,
        }

    @staticmethod
    def sync_taps():
        tap_repository_path = constants.REPOSITORY_PATH(constants.ObjectType.TAP)
        stats = RunSync.__sync(tap_repository_path)
        print("Stat for Taps : ", stats)

    @staticmethod
    def sync_targets():
        target_repository_path = constants.REPOSITORY_PATH(constants.ObjectType.TARGET)
        stats = RunSync.__sync(target_repository_path)
        print("Stat for Targets : ", stats)
