class Request:
    def __init__(self, environment, start_response):
        self.__environment = environment
        self.__start_response = start_response

        environment_map = {
            'method': 'REQUEST_METHOD',
            'path': 'PATH_INFO',
            '_raw_uri': 'RAW_URI',
            'cookie': 'HTTP_COOKIE'
        }

        for key, val in environment_map.items():
            setattr(self, key, environment.get(val))

    def get_environment(self):
        return self.__environment
