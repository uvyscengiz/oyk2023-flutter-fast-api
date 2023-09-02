import datetime

from sqlalchemy import Column, Date, String, Boolean, Integer

from .database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)
    is_done = Column(Boolean, default=False)
    created_at = Column(Date, default=datetime.date.today)
