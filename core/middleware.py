import logging

logger = logging.getLogger(__name__)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class LogIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = get_client_ip(request)

        response = self.get_response(request)

        if response.status_code == 404:
            logger.warning(f"Page not found: {request.path} from IP: {ip}")
        else:
            logger.info(f"Request made to: {request.path} from IP: {ip}")

        return response

