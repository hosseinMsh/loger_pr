import logging

logger = logging.getLogger('testlogger')

logger.error(
    'Could not find instance, doing something else',
    exc_info=True
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
