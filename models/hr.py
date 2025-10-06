from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .base import BaseModel
from .leave import leaveModel
from .performance import performanceModel

class hrModel(BaseModel):

    __tablename__ = "hr"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    department = Column(String)
    salary = Column(Integer)

    user_id = Column(Integer, ForeignKey('user.id')) 

    user = relationship('UserModel', back_populates='hr')
    leaves = relationship('leaveModel', back_populates='hr')
    performance = relationship('performanceModel', back_populates='hr')

