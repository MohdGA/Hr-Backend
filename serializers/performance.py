from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date

class performanceSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    review_date : date
    rating  : int
    comments : str

    class Config: 
        orm_mode = True


class performanceCreateSchema(BaseModel):
    review_date : date
    rating : int
    comments : str