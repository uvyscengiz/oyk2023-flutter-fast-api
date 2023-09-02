from datetime import datetime

from pydantic import BaseModel


class TodoBase(BaseModel):
    text: str
    is_done: bool


class Todo(TodoBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class TodoCreate(BaseModel):
    text: str
