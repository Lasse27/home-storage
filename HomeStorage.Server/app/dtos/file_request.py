from pydantic import BaseModel

class FileCreateRequest(BaseModel):
    filename: str
    content_type: str
    size: int
    
class FileUpdateRequest(BaseModel):
    id: str
    filename: str | None = None
    content_type: str | None = None
    size: int | None = None