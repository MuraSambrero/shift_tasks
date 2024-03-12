#from database import Base
#from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Date, UniqueConstraint, Boolean
from database.base import Base


class ShiftTask(Base):
    __tablename__ = 'shift_task'
    id = Column(Integer, primary_key=True, unique=True)
    closing_status = Column(Boolean)
    closed_at = Column(DateTime)
    shift_task = Column(String, nullable=False)
    work_center = Column(String, nullable=False)
    shift = Column(String, nullable=False)
    team_number = Column(String, nullable=False)
    batch_number = Column(Integer, nullable=False)
    batch_date = Column(Date, nullable=False)
    product = Column(String, nullable=False)
    product_code_ekn = Column(String, nullable=False)
    id_rc = Column(String, nullable=False)
    datetime_begin = Column(DateTime, nullable=False)
    datetime_end = Column(DateTime, nullable=False)
    butch_num_and_date_uniq = UniqueConstraint('batch_number', 'batch_date')
    code_product = Column(String, unique=True)
    is_aggregated = Column(Boolean, default=False)
    aggregated_at = Column(DateTime)



# shift_task = Table('shift_task', Base.metadata,
#     Column('id', Integer, primary_key=True, unique=True),
#     Column('closing_status', Boolean),
#     Column('closed_at', DateTime),
#     Column('shift_task', String, nullable=False),
#     Column('work_center', String, nullable=False),
#     Column('shift', String, nullable=False),
#     Column('team_number', String, nullable=False),
#     Column('batch_number', Integer, nullable=False),
#     Column('batch_date', Date, nullable=False),
#     Column('product', String, nullable=False),
#     Column('product_code_ekn', String, nullable=False),
#     Column('id_rc', String, nullable=False),
#     Column('datetime_begin', DateTime, nullable=False),
#     Column('datetime_end', DateTime, nullable=False),
#     UniqueConstraint('batch_number', 'batch_date', name='butch_num_and_date_uniq'),
#     Column('code_product', String, unique=True),
#     Column('is_aggregated', Boolean, default=False),
#     Column('aggregated_at', DateTime)
# )
