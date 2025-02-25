import logging
from datetime import datetime

logger = logging.getLogger('test')

def b():
    logger.error("Error message",exc_info=True)
    logger.info("Info message",exc_info=True)
    logger.warning("Warning message",exc_info=True)
    logger.debug("Debug message",exc_info=True)
    logger.critical("Critical message",exc_info=True)





def a(request):
    logger.error(
        'There was some crazy error',
        exc_info=True,
        extra={
            'datetime': str(datetime.now()),
        }
    )
