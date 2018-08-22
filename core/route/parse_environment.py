import io

routes = {
    "/home/": lambda x: "Its Home",
    "/anurag/": lambda x: "Its Anurag"
}


def parse_environment(environment, start_response):
    headers = [("Content-Type", "text/html")]
    start_response("200 Ok", headers)

    path = environment.get('PATH_INFO', '/')

    response_string = routes.get(path, lambda x: "Hello World")(start_response)

    response = io.BytesIO(response_string.encode("utf-8"))
    return response
