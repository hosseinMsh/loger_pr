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
        full_url = request.build_absolute_uri()
        ip = get_client_ip(request)
        logger.info(f"Request Method: '{request.method}', Path: ['{full_url}'], IP: ['{ip}']")
        response = self.get_response(request)
        return response





class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # اطلاعات پایه‌ای
        full_url = request.build_absolute_uri()
        method = request.method
        path = request.path
        get_params = request.GET
        post_data = request.POST
        headers = request.headers
        user = request.user
        ip = self.get_client_ip(request)

        # ثبت اطلاعات
        logger.info(f"Request method: {method}, Full URL: {full_url}, Path: {path}")
        logger.info(f"GET parameters: {get_params}")
        logger.info(f"POST data: {post_data}")
        logger.info(f"Headers: {headers}")
        logger.info(f":User  {user}, IP: {ip}")

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip