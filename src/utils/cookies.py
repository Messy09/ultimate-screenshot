thonpython
import logging
logger = logging.getLogger("cookies")

def apply_cookies(cookie_list):
    logger.info(f"Applying {len(cookie_list)} cookies...")