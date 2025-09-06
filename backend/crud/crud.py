from sqlalchemy.orm import Session
from backend.models.models import User, Travel, Budget, Hotel, Itinerary
from backend.schemas.schemas import UserCreate, TravelCreate, BudgetCreate, HotelCreate, ItineraryCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_travel(db: Session, travel: TravelCreate):
    db_travel = Travel(**travel.dict())
    db.add(db_travel)
    db.commit()
    db.refresh(db_travel)
    return db_travel

def get_travel(db: Session, travel_id: int):
    return db.query(Travel).filter(Travel.id == travel_id).first()

def create_budget(db: Session, budget: BudgetCreate):
    db_budget = Budget(**budget.dict())
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget

def get_budget(db: Session, budget_id: int):
    return db.query(Budget).filter(Budget.id == budget_id).first()

def create_hotel(db: Session, hotel: HotelCreate):
    db_hotel = Hotel(**hotel.dict())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

def get_hotel(db: Session, hotel_id: int):
    return db.query(Hotel).filter(Hotel.id == hotel_id).first()

def create_itinerary(db: Session, itinerary: ItineraryCreate):
    db_itinerary = Itinerary(**itinerary.dict())
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    return db_itinerary

def get_itinerary(db: Session, itinerary_id: int):
    return db.query(Itinerary).filter(Itinerary.id == itinerary_id).first()
