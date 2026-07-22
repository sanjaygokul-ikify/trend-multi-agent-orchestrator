class InvalidAgentError(Exception):
    def __init__(self, message: str):
        self.message = message


class InvalidTaskError(Exception):
    def __init__(self, message: str):
        self.message = message