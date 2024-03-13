from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Date,
    UniqueConstraint,
    Boolean,
)
from database.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class ShiftTask(Base):
    __tablename__ = "shift_task"
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
    code_products = relationship("CodeProduct", backref="shift_task")

    __table_args__ = (
        UniqueConstraint("batch_number", "batch_date", name="butch_num_and_date_uniq"),
    )


class CodeProduct(Base):
    __tablename__ = "code_product"
    id = Column(Integer, primary_key=True, unique=True)
    code_product = Column(String, unique=True, nullable=False)
    is_aggregated = Column(Boolean, default=False)
    aggregated_at = Column(DateTime)
    shift_task_id = Column(Integer, ForeignKey("shift_task.id"))
