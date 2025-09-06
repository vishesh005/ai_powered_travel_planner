from fastapi import FastAPI, APIRouter
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from backend.routers.user import router as user_router
from backend.routers.travel import router as travel_router
from backend.routers.budget import router as budget_router
from backend.routers.hotel import router as hotel_router
from backend.routers.itinerary import router as itinerary_router
from backend.database.database import Base, engine

app = FastAPI()

backend_router = APIRouter(prefix="/backend")

@backend_router.get("/ping")
def ping():
    return {"message": "pong"}

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(backend_router)
app.include_router(user_router)
app.include_router(travel_router)
app.include_router(budget_router)
app.include_router(hotel_router)
app.include_router(itinerary_router)

