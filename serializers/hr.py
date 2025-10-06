from pydantic import BaseModel, Field
from typing import Optional, List
from .user import UserResponseSchema
from .leave import leaveSchema
from .performance import performanceSchema

class hrSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str
    department: str
    salary: int
    user: UserResponseSchema
    leaves: List[leaveSchema]
    performance: List[performanceSchema]

    class Config:
        orm_mode = True


class hrCreateSchema(BaseModel):
    name: str
    department: str
    salary: int