from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

load_dotenv()

from app.database import SessionLocal, engine
from app import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos", response_model=List[schemas.Todo])
async def get_all_todos(db: Session = Depends(get_db)):
    return await crud.get_todos(db)

@app.get("/todos/{todo_id}", response_model=schemas.Todo)
async def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = await crud.get_todo(db, todo_id)

    if (todo == None):
        raise HTTPException(status_code=404)

    return todo

@app.post("/todos", response_model=schemas.Todo)
async def create_todo(todo_create: schemas.TodoCreate, db: Session = Depends(get_db)):
    return await crud.create_todo(db, todo_create)
