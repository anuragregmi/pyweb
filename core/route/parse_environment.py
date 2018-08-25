import io

from core.request import Request

routes = {
    "/home/": lambda x: "Its Home",
    "/anurag/": lambda x: "Its Anurag"
}


def parse_environment(environment, start_response):
    headers = [("Content-Type", "text/html")]
    start_response("200 Ok", headers)
    request = Request(environment, start_response)

    response_string = routes.get(request.path, lambda x: "Hello World")(request)
    response = io.BytesIO(response_string.encode("utf-8"))
    return response
