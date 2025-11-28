class RouteException(Exception):
    """Base exception for route errors."""

    def __init__(self, message: str, meta: dict, *args: object) -> None:
        super().__init__(*args)
        self.message = message
        self.meta = meta
        self.status = 500


class InvalidContentTypeException(RouteException):
    """Base exception for route errors."""

    def __init__(self, message: str, meta: dict, *args: object) -> None:
        super().__init__(message, meta, *args)
        self.status = 415


class InvalidContentException(RouteException):
    """Base exception for route errors."""

    def __init__(self, message: str, meta: dict, *args: object) -> None:
        super().__init__(message, meta, *args)
        self.status = 400
