from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas


app = FastAPI()


@app.get("/")
def website():
    return RedirectResponse(url="/docs")


@app.get("/tasks", response_model=schemas.TaskListResponse)
def db_card_task(db: Session = Depends(get_db)):
    query = select(models.TaskDB)
    result = db.execute(query)
    card_task = result.scalars().all()

    return {"status": "success", "message": "Список всех заданий", "card": card_task}


@app.get("/tasks/{task_id}", response_model=schemas.SingleTaskResponse)
def search_card_task(task_id: int, db: Session = Depends(get_db)):
    query = select(models.TaskDB).where(models.TaskDB.id == task_id)
    result = db.execute(query)
    card_task = result.scalar_one_or_none()

    if card_task is None:
        raise HTTPException(status_code=404, detail=f"В списке нету задания с ID: {task_id}")

    return {"status": "success", "message": f"Задание с ID: {task_id}", "card": card_task}


@app.post("/tasks", response_model=schemas.SingleTaskResponse)
def create_card_task(task_data: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_card_task = models.TaskDB(title=task_data.title, description=task_data.description)

    db.add(new_card_task)
    db.commit()
    db.refresh(new_card_task)

    return {"status": "success", "message": "Карточка задания успешно создана", "card": new_card_task}


@app.delete("/tasks/{task_id}", response_model=schemas.SingleTaskResponse)
def delete_card_task(task_id: int, db: Session = Depends(get_db)):
    query = select(models.TaskDB).where(models.TaskDB.id == task_id)
    result = db.execute(query)
    card_task = result.scalar_one_or_none()

    if card_task is None:
        raise HTTPException(status_code=404, detail=f"В списке нету задания с ID: {task_id}")

    db.delete(card_task)
    db.commit()

    return {"status": "success", "message": "Карточка задания успешно удалена"}


@app.put("/tasks/{task_id}", response_model=schemas.SingleTaskResponse)
def update_card_task(task_id: int, task_data: schemas.TaskCreate, db: Session = Depends(get_db)):
    query = select(models.TaskDB).where(models.TaskDB.id == task_id)
    result = db.execute(query)
    card_task = result.scalar_one_or_none()

    if card_task is None:
        raise HTTPException(status_code=404, detail=f"В списке нету задания с ID: {task_id}")

    card_task.title = task_data.title
    card_task.description = task_data.description

    db.commit()
    db.refresh(card_task)

    return {"status": "success", "message": "Карточка задания успешно обновлена", "card": card_task}