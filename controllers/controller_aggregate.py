from fastapi import Depends
from schemas.schemas_shift import Aggregate
from sqlalchemy.orm import Session
from database.db import get_db
from database.base import ShiftTask
from fastapi import HTTPException
from datetime import datetime


def aggregate_product(
    item: Aggregate,
    db: Session = Depends(get_db),
):
    shift_task = db.query(ShiftTask).get(item.id)
    if not shift_task:
        raise HTTPException(
            status_code=404,
            detail="Партия и дата партии с данным ID не найдена",
        )
    for cp in shift_task.code_products:
        if cp.code_product == item.code_product:
            if cp.is_aggregated:
                raise HTTPException(
                    status_code=400,
                    detail=f"unique code already used at {cp.aggregated_at}",
                )
            cp.is_aggregated = True
            cp.aggregated_at = datetime.utcnow()
            db.commit()
            return cp.code_product
    raise HTTPException(status_code=404, detail="Данный код продукции не найден")
