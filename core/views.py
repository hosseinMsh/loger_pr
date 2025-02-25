import logging
from datetime import datetime

logger = logging.getLogger('mysite')
logger.error(
    'Could not find instance, doing something else',
)
logger.info(
    'Could not find instance, doing something else',
    exc_info=True
)
logger.debug(
    'Could not find instance, doing something else',
    exc_info=True
)
logger.warning(
    'Could not find instance, doing something else',
    exc_info=True
)
def b():
    logger.error("Error message",exc_info=True)
    logger.info("Info message",exc_info=True)
    logger.warning("Warning message",exc_info=True)
    logger.debug("Debug message",exc_info=True)
    logger.critical("Critical message",exc_info=True)





def a():
    logger.error(
        'There was some crazy error',
        exc_info=True,
        extra={
            'datetime': str(datetime.now()),
        }
    )
