"""
WSGI config for DjangoProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import atexit
import logging

logger = logging.getLogger(__name__)

def log_shutdown():
    logger.info("Django application is shutting down.")

# Register the shutdown function
atexit.register(log_shutdown)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')

application = get_wsgi_application()
