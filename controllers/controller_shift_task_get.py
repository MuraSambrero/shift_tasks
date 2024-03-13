from database.base import ShiftTask
from schemas.schemas_shift import ShiftTaskPydantic
from fastapi import HTTPException, status


def get_shift_task(item_id, db):
    shift_task = db.query(ShiftTask).get(item_id)
    code_products = shift_task.code_products
    shift_task = ShiftTaskPydantic(**shift_task.__dict__)
    if not shift_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Shift task not found"
        )
    return {
        "shift_task": shift_task,
        "code_products": [c.code_product for c in code_products],
    }
