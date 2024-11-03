from unicodedata import category

from app.repositories import task_repository
from app.repositories.category_repository import category_repository


def get_categories(db):
    return category_repository.get_categories(db)


def create_category(db, category):
    return category_repository.create_category(db, category)

def get_category(db, category_id):
    return category_repository.get_category(db, category_id)

def delete_category(db, category_id):
    return category_repository.delete_category(db, category_id)
