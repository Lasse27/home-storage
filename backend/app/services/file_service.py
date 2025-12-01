from app.repositories import FileRepository, RepositoryException
from app.models.files import File
from app.services.exceptions import (
    InvalidPagingParameterException,
    InternalServerErrorException,
    NotFoundException,
)
from werkzeug.datastructures import FileStorage


class FileService:
    def __init__(self, repository: FileRepository):
        self.repository = repository

    def count_files(self) -> int:
        return self.repository.count()

    def file_exists(self, id: str) -> bool:
        return self.repository.exists(id)

    def create_file(self, file: FileStorage) -> None:
        pass

    def read_files(self, offset: int = 0, limit: int = 100) -> list:
        try:
            # Validate parameters
            if offset < 0 or limit <= 0:
                meta = {"offset": offset, "limit": limit}
                raise InvalidPagingParameterException(meta=meta)

            # Call repository method
            files: list[File] = self.repository.read(offset=offset, limit=limit)
            return files

        except RepositoryException as e:
            meta = {"offset": offset, "limit": limit, "original_error": str(e)}
            raise InternalServerErrorException(
                message="Failed to read files from repository.", meta=meta
            )

    def read_file_by_id(self, id: str) -> File:
        try:
            file: File | None = self.repository.read_by_id(id)
            if file is None:
                raise NotFoundException(message="File not found.", meta={"file_id": id})
            return file

        except RepositoryException as e:
            meta = {"file_id": id, "original_error": str(e)}
            raise InternalServerErrorException(
                message="Failed to read file from repository.", meta=meta
            )

    def update_file(self, file: File) -> None:
        if not self.repository.exists(file.id):
            meta = {"file_id": file.id}
            raise NotFoundException(message="File not found for update.", meta=meta)

        self.repository.update(file)
