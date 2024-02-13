class HttpUnprocessableContentError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "UnprocessableContet"
        self.status_code = 422
