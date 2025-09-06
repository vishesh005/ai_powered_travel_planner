from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.schemas import Travel, TravelCreate
from backend.crud.crud import create_travel, get_travel
from backend.database.database import SessionLocal

router = APIRouter(prefix="/travels", tags=["travels"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Travel)
def create_new_travel(travel: TravelCreate, db: Session = Depends(get_db)):
    return create_travel(db, travel)

@router.get("/{travel_id}", response_model=Travel)
def read_travel(travel_id: int, db: Session = Depends(get_db)):
    db_travel = get_travel(db, travel_id)
    if db_travel is None:
        raise HTTPException(status_code=404, detail="Travel not found")
    return db_travel
