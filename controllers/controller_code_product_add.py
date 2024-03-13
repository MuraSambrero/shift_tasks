from database.base import ShiftTask, CodeProduct
from fastapi import Depends
from schemas.schemas_shift import CodeProductAdd
from sqlalchemy.orm import Session
from database.db import get_db

def add_code_product(items: list[CodeProductAdd], db: Session = Depends(get_db)):
    list_status = []
    for item in items:
        shift_task = (
            db.query(ShiftTask)
            .filter(
                ShiftTask.batch_number == item.batch_number,
                ShiftTask.batch_date == item.batch_date,
            )
            .first()
        )
        status = f'Уникальный код добавлен к партии ({item.batch_number}, {item.batch_date})'
        code_product = db.query(CodeProduct).filter(CodeProduct.code_product == item.code_product)
        if not shift_task:
            status = f'Такого номера партии({item.batch_number}, {item.batch_date}) не существует'
        elif code_product:
            status = f'Данный код продукции {item.code_product} уже существует'
        else:
            code_product = CodeProduct(
                code_product=item.code_product,
                shift_task_id=shift_task.id,
            )
            db.add(code_product)
            db.commit()
            db.refresh(code_product)
        list_status.append({'Статус': status})
    return list_status