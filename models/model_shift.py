from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Date


class ShiftTask(Base):
    closing_status = Column(Integer, primary_key=True, index=True, unique=True)
    closed_at = Column(DateTime)
    shift_task = Column(String)
    work_center = Column(String)
    shift = Column(String)
    team_number = Column(String)
    batch_number = Column(Integer)
    batch_date = Column(Date)
    product = Column(String)
    product_code_ekn = Column(String)
    id_rc = Column(String)
    datetime_begin = Column(DateTime)
    datetime_end = Column(DateTime)
