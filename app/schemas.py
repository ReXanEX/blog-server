# This file defines Pydantic schemas for request and response validation
from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True  # allows to work with ORM-models
