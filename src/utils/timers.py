thonpython
import time
import logging

logger = logging.getLogger("timers")

def wait_for_load(seconds: float = 1.0):
    logger.info(f"Waiting for page load: {seconds}s...")
    time.sleep(seconds)