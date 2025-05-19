from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from app.db.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(128), default="password", nullable=False)
    is_active = Column(Integer, default=1, nullable=False)
    is_superuser = Column(Integer, default=0, nullable=False)
    is_verified = Column(Integer, default=0, nullable=False)
    # Consider using Boolean for flags:
    is_deleted = Column(Boolean, default=False)
    is_blocked = Column(Boolean, default=False)        
    
