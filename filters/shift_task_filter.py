from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Optional
from database.base import ShiftTask
from datetime import date, datetime


class ShiftTaskFilter(Filter):
    closing_status: Optional[bool] = None
    shift_task: Optional[str] = None
    work_center: Optional[str] = None
    shift: Optional[str] = None
    team_number: Optional[str] = None
    batch_number: Optional[int] = None
    batch_date: Optional[date] = None
    batch_date__lte: Optional[date] = None
    batch_date__gte: Optional[date] = None
    product: Optional[str] = None
    product_code_ekn: Optional[str] = None
    id_rc__like: Optional[str] = None
    datetime_begin: Optional[datetime] = None
    datetime_end: Optional[datetime] = None

    class Constants(Filter.Constants):
        model = ShiftTask
