from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .base import BaseModel


class performanceModel(BaseModel):
    
    __tablename__ = 'performance'

    id = Column(Integer, primary_key=True, index=True)
    review_date = Column(Date)
    rating = Column(Integer)
    comments = Column(String)

    hr_id = Column(Integer, ForeignKey('hr.id'))

    hr = relationship('hrModel', back_populates='performance')