from http.client import responses


class Response:
    def __init__(self, response_string="", status_code=200):
        self.response_string = response_string
        self.status_code = 200

    @property
    def response_phrase(self):
        return responses.get(self.status_code, "")
