"""
The main entry point to the program.
"""
# Handle imports
import logging_config

# Handle vars

# Run code
logger = logging_config.get_logger("app")

logger.debug("Debug")
logger.info("Info")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")