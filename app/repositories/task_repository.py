from sqlmodel import Session
from app.models.models import Task
from app.schema.task_schema import TaskCreate, TaskBase


def create_task_repo(task:TaskCreate , db:Session):
    task_db =Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        due_date=task.due_date,
        status=task.status,
        user_id=task.user_id,
    )
    db.add(task_db)
    db.commit()
    db.refresh(task_db)
    return task_db


def get_tasks(db):
    return db.query(Task).all()

def get_task_by_id(db, id_task: int)-> Task:
    return db.query(Task).filter(Task.id == id_task).first()


def update_task(db: Session, task: Task) -> Task:
        db.add(task)
        db.commit()
        db.refresh(task)
        return task