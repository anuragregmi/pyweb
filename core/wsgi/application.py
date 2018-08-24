from ..route.parse_environment import parse_environment
import os


class Wsgi:

    def __call__(self, environment, start_response):
        return parse_environment(environment, start_response)
