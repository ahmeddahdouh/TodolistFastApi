from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.models import Task
from app.repositories import task_repository
from app.repositories.user_repository import get_user_by_id
from app.schema.task_schema import TaskCreate
from app.repositories.task_repository import create_task_repo

def create_task(db:Session,task:TaskCreate):
    if not get_user_by_id(db, task.user_id):
        raise HTTPException(status_code=400, detail="Utilisateur n'existe pas ")
    return create_task_repo(task,db)


def get_tasks(db:Session,user_id:int):
    return task_repository.get_tasks(db)

def get_task_by_id(db: Session, id_task: int):
    task = task_repository.get_task_by_id(db, id_task)
    if not task:
        raise HTTPException(status_code=404, detail="Cette tâche n'existe pas dans la base de données.")
    return task


def update_task(db: Session,task_id: int,  task_data: TaskCreate) -> Task:
    task = task_repository.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in task_data.model_dump(exclude_unset=True).items():
        setattr(task, key, value)

    return task_repository.update_task(db, task)