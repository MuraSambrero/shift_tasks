from fastapi import APIRouter

router_shifts = APIRouter()

@router_shifts.post("/add_shift_task") # добавление списка сменных заданий
def tasks_add():
    return {"message": "shift"}

@router_shifts.post("/") # получение списка сменных заданий
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

