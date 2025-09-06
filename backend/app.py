from fastapi import FastAPI, APIRouter
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

REACT_BUILD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend/build"))

app.mount("/frontend/static", StaticFiles(directory=os.path.join(REACT_BUILD_DIR, "static")), name="static")

@app.get("/frontend")
def serve_react_index():
    index_path = os.path.join(REACT_BUILD_DIR, "index.html")
    return FileResponse(index_path)

backend_router = APIRouter(prefix="/backend")

@backend_router.get("/ping")
def ping():
    return {"message": "pong"}

app.include_router(backend_router)