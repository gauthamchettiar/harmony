from utils.crawlers.github import Github


class Crawler:
    @staticmethod
    def select_crawler(url: str):
        return Github(url)
