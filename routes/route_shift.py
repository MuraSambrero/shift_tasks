from fastapi import APIRouter, Depends
from schemas.schemas_shift import ShiftTaskAdd, ShiftTaskPydantic
from sqlalchemy.orm import Session
from database.db import get_db
from controllers.controller_shift_task_add import add_list_shift_task
from controllers.controller_shift_task_get import get_shift_task
from fastapi import Query

router_shifts = APIRouter()


@router_shifts.post("/add_shift_task")  # добавление списка сменных заданий
def tasks_add(items: list[ShiftTaskAdd], db: Session = Depends(get_db)) -> list:
    return add_list_shift_task(items, db)


@router_shifts.get("/get_task") # получение сменного задания по id
def get_task(
    item_id: int = Query(),
    db: Session = Depends(get_db),
):
    return get_shift_task(item_id, db)


@router_shifts.get("/")  # получение списка сменных заданий
def tasks_list():
    return {"message": "tasks_list"}


@router_shifts.put("/update_task") # изменение сменного задания по id
def update_task():
    return {"message": "update_task"}


@router_shifts.post("/aggregate") # создание продукции и привязка ее к партии
def aggregate():
    return {"message": "aggregate"}
