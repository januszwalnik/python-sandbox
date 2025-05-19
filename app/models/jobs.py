from sqlalchemy import Column, Integer, String

from app.db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy import DateTime


class Jobs(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)