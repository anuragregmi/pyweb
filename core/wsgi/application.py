from ..route.parse_environment import parse_environ


class Wsgi:
    def __call__(self, environment, start_response):
        return parse_environ(environment, start_response)
