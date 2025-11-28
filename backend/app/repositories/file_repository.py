from app.models.files import File
from sqlalchemy.orm import Session


class FileRepository:

    ## Builtin Methods ##

    def __init__(self, session: Session):
        self.session = session

    ## Meta Methods ##

    def count(self) -> int:
        return self.session.query(File).count()

    def exists(self, id: str) -> bool:
        stmt = self.session.select(
            self.session.exists().where(File.id == id)
        )
        return self.session.scalar(stmt)

    ## Create Methods ##

    def create(self, file: File) -> None:
        self.session.add(file)
        self.session.commit()

    ## Read Methods ##

    def read(self, offset: int = 0, limit: int = 100) -> list[File]:
        return self.session.query(File).offset(offset).limit(limit).all()

    def read_by_id(self, id: str) -> File | None:
        return self.session.query(File).filter(File.id == id).first()

    ## Update Methods ##

    def update(self, file: File) -> None:
        self.session.merge(file)
        self.session.commit()

    ## Delete Methods ##

    def delete(self, file: File) -> None:
        self.session.delete(file)
        self.session.commit()
