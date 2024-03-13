from database.base import ShiftTask
from fastapi import HTTPException, status
from datetime import datetime


def shift_task_update(item, item_id, db):
    shift_task = db.query(ShiftTask).get(item_id)
    if not shift_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Shift task not found"
        )
    for key, value in item.dict().items():
        setattr(shift_task, key, value) if value else None
    if shift_task.closing_status:
        shift_task.closed_at = datetime.utcnow()
    else:
        shift_task.closed_at = None
    db.commit()
    db.refresh(shift_task)
    return shift_task
