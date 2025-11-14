thonpython
import logging
import time

logger = logging.getLogger("scroll")

def auto_scroll(steps: int = 5, delay: float = 0.1):
    logger.info(f"Auto-scrolling page ({steps} steps)...")
    for _ in range(steps):
        time.sleep(delay)