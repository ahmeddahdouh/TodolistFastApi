from fastapi import APIRouter, HTTPException
from sqlalchemy.sql.functions import user

from app.core.config import db_dependency
from app.models.models import Task
from app.repositories.user_repository import get_user_by_id
from app.schema.task_schema import TaskCreate
from app.services import task_service

task_router = APIRouter()

@task_router.post("/task")
async def create_task(task:TaskCreate,db : db_dependency):
    return task_service.create_task(db,task)


@task_router.get("/task")
async def get_tasks(db : db_dependency):
    return task_service.get_tasks(db)

@task_router.get("/task/{task_id}")
async def get_task(task_id: int, db: db_dependency):
    task = task_service.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@task_router.put("/task/{task_id}")
async def update_task(task_id: int, task_data: TaskCreate, db:db_dependency):
    print("\n \n"+ task_data.title +"\n \n")
    try:
        updated_task = task_service.update_task(db, task_id, task_data)
        return updated_task
    except HTTPException as e:
        raise e
