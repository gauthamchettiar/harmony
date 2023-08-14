import sys
from utils import dump, fetch
from utils.run import RunSync
from loguru import logger

logger.remove(0)
logger.add(sys.stderr, level="INFO")
logger.add("logs/file_{time}.log", level="DEBUG")

if __name__ == "__main__":
    RunSync.sync_taps()
    RunSync.sync_targets()
