from fastapi import APIRouter, Depends
from schemas.schemas_shift import (
    ShiftTaskAdd,
    ShiftTaskUpdate,
    CodeProductAdd,
    Aggregate
)
from sqlalchemy.orm import Session
from database.db import get_db
from controllers.controller_shift_task_add import add_list_shift_task
from controllers.controller_shift_task_get import get_shift_task
from controllers.controller_shift_task_filter import get_shift_task_list
from controllers.controller_shift_task_update import shift_task_update
from controllers.controller_code_product_add import add_code_product
from controllers.controller_aggregate import aggregate_product
from fastapi import Query
from fastapi_filter import FilterDepends
from filters.shift_task_filter import ShiftTaskFilter

router_shifts = APIRouter()


@router_shifts.post("/add_shift_task")  # добавление списка сменных заданий
def tasks_add(items: list[ShiftTaskAdd], db: Session = Depends(get_db)) -> list:
    return add_list_shift_task(items, db)


@router_shifts.get("/get_task")  # получение сменного задания по id
def get_task(
    item_id: int = Query(),
    db: Session = Depends(get_db),
):
    return get_shift_task(item_id, db)


@router_shifts.post("/")  # получение списка сменных заданий
def tasks_list(
    shift_task_filter: ShiftTaskFilter = FilterDepends(ShiftTaskFilter),
    db: Session = Depends(get_db),
):
    return get_shift_task_list(shift_task_filter, db)


@router_shifts.patch("/update_task")  # изменение сменного задания по id
def update_task(
    item: ShiftTaskUpdate,
    item_id: int = Query(),
    db: Session = Depends(get_db),
):
    return shift_task_update(item, item_id, db)


@router_shifts.post("/code_product_add")  # создание продукции и привязка ее к партии
def code_product_add(items: list[CodeProductAdd], db: Session = Depends(get_db)):
    return add_code_product(items, db)


@router_shifts.post("/aggregate")  # аггрегация продукции
def aggregate(item: Aggregate, db: Session = Depends(get_db)):
    return aggregate_product(item, db)
