from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .files import File, FileTag, Tag
