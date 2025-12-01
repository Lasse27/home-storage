class ServiceException(Exception):
    """Base exception class for service layer errors."""

    def __init__(self, message: str, meta: dict, *args: object) -> None:
        super().__init__(*args)
        self.message = message
        self.status = 500
        self.meta = meta


class InvalidPagingParameterException(ServiceException):
    """Exception raised for invalid parameters in requests."""

    def __init__(self, meta: dict, *args: object) -> None:
        super().__init__(
            "Invalid paging parameters. Offset must be non-negative and limit must be positive.",
            meta,
            *args,
        )
        self.status = 400


class NotFoundException(ServiceException):
    """Exception raised when a requested resource is not found."""

    def __init__(self, message: str, meta: dict, *args: object) -> None:
        super().__init__(message, meta, *args)
        self.status = 404


class ConflictException(ServiceException):
    """Exception raised for conflicts, such as duplicate entries."""

    def __init__(self, message: str, meta: dict, *args: object) -> None:
        super().__init__(message, meta, *args)
        self.status = 409


class UnsupportedMediaTypeException(ServiceException):
    """Exception raised for unsupported media types."""

    def __init__(self, message: str, meta: dict, *args: object) -> None:
        super().__init__(message, meta, *args)
        self.status = 415


class InternalServerErrorException(ServiceException):
    """Exception raised for internal server errors."""

    def __init__(self, message: str, meta: dict, *args: object) -> None:
        super().__init__(message, meta, *args)
        self.status = 500
