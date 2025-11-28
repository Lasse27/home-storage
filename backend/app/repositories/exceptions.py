class RepositoryException(Exception):
    """Base exception for repository errors."""
    def __init__(self, message: str, *args: object) -> None:
        super().__init__(*args)
        self.message = message