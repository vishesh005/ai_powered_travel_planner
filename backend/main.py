from fastapi import FastAPI, APIRouter
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

backend_router = APIRouter(prefix="/backend")

@backend_router.get("/ping")
def ping():
    return {"message": "pong"}

app.include_router(backend_router)

