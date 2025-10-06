from sqlalchemy import Column, Integer, String,Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .base import BaseModel


class leaveModel(BaseModel):

    __tablename__= "leaves"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String,nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)

    hr_id = Column(Integer, ForeignKey('hr.id'))

    hr = relationship('hrModel',back_populates='leaves')
    