from database.base import ShiftTask
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from schemas.schemas_shift import ShiftTaskAdd
from fastapi import Depends
from sqlalchemy.orm import Session
from database.db import get_db


def add_list_shift_task(
    items: list[ShiftTaskAdd],
    db: Session = Depends(get_db),
) -> list:
    status_add_list = []
    for item in items:
        shift_task = ShiftTask(**item.model_dump())
        status_add = add_shift_task(shift_task, db)
        status_add_list.append(status_add)
    return status_add_list


def add_shift_task(task: ShiftTask, db) -> str:
    db.add(task)
    try:
        db.commit()
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            db.rollback()
            return (
                f"Данное задание {task.batch_number}, {task.batch_date} уже существует"
            )
        else:
            raise e
    db.refresh(task)
    return f"Задание {task.batch_number}, {task.batch_date} успешно добавлено в базу."
