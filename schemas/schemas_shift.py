from pydantic import BaseModel, Field
from datetime import datetime, date

class ShiftAdd(BaseModel):
    closing_status: bool = Field(alias='СтатусЗакрытия')
    shift_task: str = Field(alias='ПредставлениеЗаданияНаСмену')
    work_center: str = Field(alias='Линия')
    shift: str = Field(alias='Смена')
    team_number: str = Field(alias='Бригада')
    batch_number: int = Field(alias='НомерПартии')
    batch_date: date = Field(alias='ДатаПартии')
    product: str = Field(alias='Номенклатура')
    product_code_ekn: str = Field(alias='КодЕКН')
    id_rc: str = Field(alias='ИдентификаторРЦ')
    datetime_begin: datetime = Field(alias='ДатаВремяНачалаСмены')
    datetime_end: datetime = Field(alias='ДатаВремяОкончанияСмены')

