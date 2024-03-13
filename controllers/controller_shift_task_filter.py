from sqlalchemy.orm import Session
from database.db import get_db
from database.base import ShiftTask
from filters.shift_task_filter import ShiftTaskFilter
from fastapi import Depends
from fastapi_filter import FilterDepends
from sqlalchemy import select


def get_shift_task_list(
    shift_task_filter: ShiftTaskFilter = FilterDepends(ShiftTaskFilter),
    db: Session = Depends(get_db),
):
    shift_task_all = select(ShiftTask)
    shift_task_all = shift_task_filter.filter(shift_task_all)
    result = db.execute(shift_task_all)
    return result.scalars().all()


# @app.get("/users", response_model=List[UserOut])
# async def get_users(
#     user_filter: UserFilter = FilterDepends(UserFilter),
#     db: AsyncSession = Depends(get_db),
# ) -> Any:
#     query = select(User).join(Address)
#     query = user_filter.filter(query)
#     query = user_filter.sort(query)
#     result = await db.execute(query)
#     return result.scalars().all()
