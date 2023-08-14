from utils import dump, fetch
from utils.run import RunSync
from loguru import logger

logger.add("logs/file_{time}.log")

if __name__ == "__main__":
    RunSync.sync_taps()
    RunSync.sync_targets()
