from app.models.files import File
from app.extensions import db


class FileRepository:
    def count(self) -> int:
        return File.query.count()

    def exists(self, id: str) -> bool:
        return File.query.exists()

    def create(self, file: File) -> None:
        db.session.add(file)
        db.session.commit()

    def read(self, offset: int = 0, limit: int = 100) -> list[File]:
        return File.query.offset(offset).limit(limit).all()

    def read_by_id(self, id: str) -> File | None:
        return File.query.get(id)

    def update(self, file: File) -> None:
        db.session.merge(file)
        db.session.commit()

    def delete(self, file: File) -> None:
        db.session.delete(file)
        db.session.commit()
