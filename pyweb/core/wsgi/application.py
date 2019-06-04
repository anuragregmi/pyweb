import io

from ..conf import settings
from ..route.routes import get_routes
from ..request import Request


class Wsgi:

    default_headers = [("Content-Type", "text/html")]

    def __init__(self):
        self.routes = get_routes(settings.ROUTES)

    def __call__(self, environment, start_response):
        return self.parse_environment(environment, start_response)

    def parse_environment(self, environment, start_response):
        request = Request(environment, start_response)

        view_function = self.routes.get(request.path, None)
        if not view_function:
            start_response("404 Not Found", [])
            response_string = "Requested page was not found in this server."
        else:
            start_response("200 Ok", self.default_headers)
            response_string = view_function(request)

        response = io.BytesIO(response_string.encode("utf-8"))
        return response
