from pydantic import BaseModel, Field
from datetime import datetime, date


class ShiftTaskAdd(BaseModel):
    closing_status: bool = Field(alias="СтатусЗакрытия")
    shift_task: str = Field(alias="ПредставлениеЗаданияНаСмену")
    work_center: str = Field(alias="Линия")
    shift: str = Field(alias="Смена")
    team_number: str = Field(alias="Бригада")
    batch_number: int = Field(alias="НомерПартии")
    batch_date: date = Field(alias="ДатаПартии")
    product: str = Field(alias="Номенклатура")
    product_code_ekn: str = Field(alias="КодЕКН")
    id_rc: str = Field(alias="ИдентификаторРЦ")
    datetime_begin: datetime = Field(alias="ДатаВремяНачалаСмены")
    datetime_end: datetime = Field(alias="ДатаВремяОкончанияСмены")


class ShiftTaskPydantic(BaseModel):
    id: int = Field(serialization_alias="ID")
    closed_at: datetime | None = Field(
        serialization_alias="ВремяЗакрытия",
        default=None,
    )
    closing_status: bool = Field(serialization_alias="СтатусЗакрытия")
    shift_task: str = Field(serialization_alias="ПредставлениеЗаданияНаСмену")
    work_center: str = Field(serialization_alias="Линия")
    shift: str = Field(serialization_alias="Смена")
    team_number: str = Field(serialization_alias="Бригада")
    batch_number: int = Field(serialization_alias="НомерПартии")
    batch_date: date = Field(serialization_alias="ДатаПартии")
    product: str = Field(serialization_alias="Номенклатура")
    product_code_ekn: str = Field(serialization_alias="КодЕКН")
    id_rc: str = Field(serialization_alias="ИдентификаторРЦ")
    datetime_begin: datetime = Field(serialization_alias="ДатаВремяНачалаСмены")
    datetime_end: datetime = Field(serialization_alias="ДатаВремяОкончанияСмены")
