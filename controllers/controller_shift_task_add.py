from database.base import ShiftTask
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from schemas.schemas_shift import ShiftTaskAdd



def add_list_shift_task(items: list[ShiftTaskAdd], db) -> list:
    status_add_list = []
    for item in items:
        shift_task = ShiftTask(
            closing_status = item.closing_status,
            shift_task = item.shift_task,
            work_center = item.work_center,
            shift = item.shift,
            team_number = item.team_number,
            batch_number = item.batch_number,
            batch_date = item.batch_date,
            product = item.product,
            product_code_ekn = item.product_code_ekn,
            id_rc = item.id_rc,
            datetime_begin = item.datetime_begin,
            datetime_end = item.datetime_end,
        )
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
            return f'Данное задание {task.batch_number}, {task.batch_date} уже существует'
        else:
            raise e
    db.refresh(task)
    return f'Задание {task.batch_number}, {task.batch_date} успешно добавлено в базу.'

