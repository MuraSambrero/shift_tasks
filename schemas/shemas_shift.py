from pydantic import BaseModel

class ShiftsAdd(BaseModel):
    shift_tasks: list[str]