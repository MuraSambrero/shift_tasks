from fastapi import APIRouter, Depends
from schemas.schemas_shift import ShiftAdd
from sqlalchemy.orm import Session
from database.db import get_db
from database.base import ShiftTask

router_shifts = APIRouter()

@router_shifts.post("/add_shift_task") # добавление списка сменных заданий
def tasks_add(items: list[ShiftAdd], db: Session = Depends(get_db)):
    tasks = [ShiftTask(**item) for item in items]
    db.add_all(tasks)
    db.commit()
    db.refresh(tasks)
    return tasks

@router_shifts.get("/") # получение списка сменных заданий
def tasks_list():
    return {"message": "tasks_list"}

@router_shifts.get("/get_task")
def get_task(): # получение сменного задания по id
    return {"message": "get_task"}

@router_shifts.put("/update_task")
def update_task(): # изменение сменного задания по id
    return {"message": "update_task"}

@router_shifts.post("/aggregate")
def aggregate(): # создание продукции и привязка ее к партии
    return {"message": "aggregate"}

