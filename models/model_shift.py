#from database import Base
from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, Date, UniqueConstraint, ForeignKey, TIMESTAMP

metadata = MetaData()



shift_task = Table('shift_task', metadata,
    Column('closing_status', Integer, primary_key=True, index=True, unique=True),
    Column('closed_at', TIMESTAMP, nullable=False, default=datetime.utcnow),
    Column('shift_task', String),
    Column('work_center', String),
    Column('shift', String),
    Column('team_number', String),
    Column('batch_number', Integer),
    Column('batch_date', Date),
    Column('product', String),
    Column('product_code_ekn', String),
    Column('id_rc', String),
    Column('datetime_begin', DateTime),
    Column('datetime_end', DateTime),
    UniqueConstraint('butch_number', 'batch_date', String, name='butch_num_and_date_uniq')
)

code_product = Table('code_product', metadata,
    Column('code_product', String, primary_key=True, index=True, unique=True),
    Column('is_aggregated', String),
    Column('aggregated_at', DateTime),
    Column('shift_task_butch_num_and_date', String, ForeignKey('shift_task.butch_num_and_date_uniq'))
)



# class ShiftTask(Base):
#     closing_status = Column(Integer, primary_key=True, index=True, unique=True)
#     closed_at = Column(DateTime)
#     shift_task = Column(String)
#     work_center = Column(String)
#     shift = Column(String)
#     team_number = Column(String)
#     batch_number = Column(Integer)
#     batch_date = Column(Date)
#     product = Column(String)
#     product_code_ekn = Column(String)
#     id_rc = Column(String)
#     datetime_begin = Column(DateTime)
#     datetime_end = Column(DateTime)


# class CodeProduct(Base):
#     code_product = Column(String, primary_key=True, index=True, unique=True)
#     is_aggregated = Column(String)
#     aggregated_at = Column(DateTime)