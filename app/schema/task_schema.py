from datetime import datetime

from fastapi.openapi.models import Schema
from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str
    due_date: datetime
    priority: int
    status : str
    user_id : int
    class Config:
        orm_mode = True

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    title : str
