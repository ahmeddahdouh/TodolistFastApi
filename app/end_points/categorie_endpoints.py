from fastapi import APIRouter

from app.core.config import db_dependency
from app.schema.category_schema import CategoryBase
from app.services import category_service

category_router = APIRouter()


@category_router.get("/categories",tags=['categories'])
async def get_categories(db: db_dependency):
    return category_service.get_categories(db)


@category_router.post("/category",tags=['categories'])
async def create_category(db: db_dependency,category:CategoryBase):
    return category_service.create_category(db,category)

@category_router.get("/category/{category_id}",tags=['categories'])
async def get_category(db: db_dependency,category_id):
    return category_service.get_category(db,category_id)

@category_router.delete("/category",tags=['categories'])
async def delete_category(db: db_dependency,category_id):
    return category_service.delete_category(db,category_id)