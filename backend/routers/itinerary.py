from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.schemas import Itinerary, ItineraryCreate
from backend.crud.crud import create_itinerary, get_itinerary
from backend.database.database import SessionLocal

router = APIRouter(prefix="/itineraries", tags=["itineraries"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Itinerary)
def create_new_itinerary(itinerary: ItineraryCreate, db: Session = Depends(get_db)):
    return create_itinerary(db, itinerary)

@router.get("/{itinerary_id}", response_model=Itinerary)
def read_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    db_itinerary = get_itinerary(db, itinerary_id)
    if db_itinerary is None:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return db_itinerary
