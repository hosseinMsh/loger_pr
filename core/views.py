import logging
from datetime import datetime

from django.http import HttpResponse

logger = logging.getLogger(__name__)

def b(request):
    logger.error("Error message",exc_info=True)
    logger.info("Info message",exc_info=True)
    logger.warning("Warning message",exc_info=True)
    logger.debug("Debug message",exc_info=True)
    logger.critical("Critical message",exc_info=True)
    return HttpResponse("Hello, world. You're at the polls index.")




def a(request):
    logger.error(
        'There was some crazy error',
        exc_info=True,
        extra={
            'datetime': str(datetime.now()),
        }
    )
