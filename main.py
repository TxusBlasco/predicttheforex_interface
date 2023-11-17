from fastapi import FastAPI
from core.infrastructure.controllers.dashboard import home

app = FastAPI()
app.include_router(home)
