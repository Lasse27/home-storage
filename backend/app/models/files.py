import uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from . import Base


class File(Base):
    __tablename__ = "files"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    filename_original: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    filename_disk: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    storage_path: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    mime_type: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    size: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        nullable=False
    )

    # Relationships
    file_tags = relationship(
        "FileTag",
        back_populates="file",
        # Wenn die Datei gelöscht wird, lösche auch die zugehörigen Tags in der Verknüpfungstabelle
        cascade="all, delete-orphan"
    )


class FileTag(Base):
    __tablename__ = "file_tags"

    # Columns
    file_id: Mapped[str] = mapped_column(
        ForeignKey("files.id"),
        primary_key=True
    )

    tag_id: Mapped[str] = mapped_column(
        ForeignKey("tags.id"),
        primary_key=True
    )

    # Relationships
    file = relationship("File", back_populates="file_tags")
    tag = relationship("Tag", back_populates="file_tags")


class Tag(Base):

    __tablename__ = "tags"

    # Columns
    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        index=True,
        default=lambda: str(uuid.uuid4())
    )

    name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True
    )

    color: Mapped[str] = mapped_column(
        String(255)
    )

    # Relationships
    file_tags = relationship("FileTag", back_populates="tag")
