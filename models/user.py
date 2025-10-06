from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jwt
from models.hr import hrModel

from config.environment import secret

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class UserModel(BaseModel):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    hr = relationship('hrModel', back_populates='user')

    def set_password(self, password: str):
        self.password_hash = pwd_context.hash(password)
    
    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password_hash)
    
    def generate_token(self):

        payload = {
            "exp": datetime.now(timezone.utc) + timedelta(days=1),
            "iat": datetime.now(timezone.utc),
            "sub": str(self.id),
            'username': self.username
        }

        token = jwt.encode(payload, secret, algorithm="HS256")

        return token
