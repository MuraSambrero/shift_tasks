#from database import Base
from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, Date, UniqueConstraint, Boolean, TIMESTAMP

metadata = MetaData()

shift_task = Table('shift_task', metadata,
    Column('id', Integer, primary_key=True, unique=True),
    Column('closing_status', Boolean),
    Column('closed_at', TIMESTAMP, nullable=False, default=datetime.utcnow),
    Column('shift_task', String, nullable=False),
    Column('work_center', String, nullable=False),
    Column('shift', String, nullable=False),
    Column('team_number', String, nullable=False),
    Column('batch_number', Integer, nullable=False),
    Column('batch_date', Date, nullable=False),
    Column('product', String, nullable=False),
    Column('product_code_ekn', String, nullable=False),
    Column('id_rc', String, nullable=False),
    Column('datetime_begin', DateTime, nullable=False),
    Column('datetime_end', DateTime, nullable=False),
    UniqueConstraint('batch_number', 'batch_date', name='butch_num_and_date_uniq'),
    Column('code_product', String, unique=True),
    Column('is_aggregated', Boolean, default=False),
    Column('aggregated_at', DateTime)
)
