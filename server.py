from fastapi import FastAPI

# Entities
from src.infra.database.entities.models import *

# Routers
from src.routers.user_router import router as user_router
from src.routers.board_router import router as board_router
from src.routers.task_router import router as task_router

app = FastAPI()

app.include_router(user_router)
app.include_router(board_router)
app.include_router(task_router)

    

