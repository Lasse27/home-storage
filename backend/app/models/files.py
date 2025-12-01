import uuid
from datetime import datetime
from app.extensions import db


class File(db.Model):
    # Meta
    __tablename__ = "files"

    # Columns
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    filename_original = db.Column(db.String(255), nullable=False)
    filename_disk = db.Column(db.String(255), nullable=False)
    storage_path = db.Column(db.String, nullable=False)
    mime_type = db.Column(db.String(255), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Relationships
    file_tags = db.relationship(
        "FileTag", back_populates="file", cascade="all, delete-orphan", lazy=True
    )


class FileTag(db.Model):
    # Meta
    __tablename__ = "file_tags"

    # Columns
    file_id = db.Column(db.String(36), db.ForeignKey("files.id"), primary_key=True)
    tag_id = db.Column(db.String(36), db.ForeignKey("tags.id"), primary_key=True)

    # Relationships
    file = db.relationship("File", back_populates="file_tags")
    tag = db.relationship("Tag", back_populates="file_tags")


class Tag(db.Model):
    # Meta
    __tablename__ = "tags"

    # Columns
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(255), unique=True, index=True, nullable=False)
    color = db.Column(db.String(255), nullable=True)

    # Relationships
    file_tags = db.relationship("FileTag", back_populates="tag", lazy=True)
