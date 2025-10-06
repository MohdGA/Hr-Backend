from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date

class leaveSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    type: str
    start_date: date
    end_date: date
    status: str

    class Config:
        orm_mode = True

class leaveCreateSchema(BaseModel):
    type: str
    start_date: date
    end_date: date
    status: str

