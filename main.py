from asyncio import tasks

from fastapi import FastAPI
from app.core.database import engine
from app.end_points.tasks_end_points import task_router
from app.end_points.users_end_points import router
from app.models import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(router)
app.include_router(task_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=800, reload=True)
