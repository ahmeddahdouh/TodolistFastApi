import datetime

from sqlalchemy import Integer, String, Column, ForeignKey, Float, ARRAY, DateTime
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String, nullable=False)
    vocal_data = Column(ARRAY(Float), nullable=True)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    due_date = Column(DateTime)
    priority = Column(Integer, nullable=False)
    status = Column(String(15), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

