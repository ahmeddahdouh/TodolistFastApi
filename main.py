from asyncio import tasks

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.database import engine
from app.end_points.categorie_endpoints import category_router
from app.end_points.tasks_end_points import task_router
from app.end_points.users_end_points import router
from app.models import models
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise toutes les origines (remplacer "*" par les origines spécifiques si nécessaire)
    allow_credentials=True,
    allow_methods=["*"],  # Permet toutes les méthodes HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permet tous les types d'en-têtes
)



app.mount("/static", StaticFiles(directory="static"), name="static")

models.Base.metadata.create_all(bind=engine)
app.include_router(router)
app.include_router(task_router)
app.include_router(category_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=800, reload=True)
