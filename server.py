from fastapi import FastAPI

# DB config
from src.infra.database.config.db_config import create_db, get_db

# Entities
from src.infra.database.entities.models import *

# Routers
from src.routers.user_router import router as user_router


create_db()

app = FastAPI()

app.include_router(user_router)

