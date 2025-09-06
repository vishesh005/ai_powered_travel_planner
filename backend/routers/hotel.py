from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.schemas import Hotel, HotelCreate
from backend.crud.crud import create_hotel, get_hotel
from backend.database.database import SessionLocal

router = APIRouter(prefix="/hotels", tags=["hotels"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Hotel)
def create_new_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    return create_hotel(db, hotel)

@router.get("/{hotel_id}", response_model=Hotel)
def read_hotel(hotel_id: int, db: Session = Depends(get_db)):
    db_hotel = get_hotel(db, hotel_id)
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return db_hotel
