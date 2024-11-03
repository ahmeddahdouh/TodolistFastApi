from dns.e164 import query

from app.models.models import Category
from fastapi import HTTPException
from sqlmodel import Session
from app.models.models import Task
from app.schema.category_schema import CategoryBase
from app.schema.task_schema import TaskCreate, TaskBase


class category_repository:

    def get_categories(db):
        return db.query(Category).all()

    def create_category(db,category:CategoryBase):
        category_db = Category(name=category.name)
        db.add(category_db)
        db.commit()
        db.refresh(category_db)
        return category_db

    def get_category(db,category_id):
        return db.query(Category).filter(Category.id == category_id).first()

    def delete_category(db,category_id):
        category= db.query(Category).filter(Category.id == category_id).first()
        if category:
            db.delete(category)
            db.commit()
            return {'message':f'Category {category_id} {category.name} deleted'}
        else:
            return {'message':f'Category  not found'}



