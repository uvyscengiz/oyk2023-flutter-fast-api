from sqlalchemy.orm import Session
from . import models, schemas


async def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


async def get_todos(db: Session):
    return db.query(models.Todo).all()


async def create_todo(db: Session, todo_create: schemas.TodoCreate):
    db_todo = models.Todo(
        text=todo_create.text,
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
