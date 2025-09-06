from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class TravelBase(BaseModel):
    destination: str
    start_date: datetime
    end_date: datetime

class TravelCreate(TravelBase):
    user_id: int

class Travel(TravelBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True

class BudgetBase(BaseModel):
    amount: float

class BudgetCreate(BudgetBase):
    travel_id: int

class Budget(BudgetBase):
    id: int
    travel_id: int
    class Config:
        orm_mode = True

class HotelBase(BaseModel):
    name: str
    address: str
    price_per_night: float

class HotelCreate(HotelBase):
    travel_id: int

class Hotel(HotelBase):
    id: int
    travel_id: int
    class Config:
        orm_mode = True

class ItineraryBase(BaseModel):
    day: int
    activity: str

class ItineraryCreate(ItineraryBase):
    travel_id: int

class Itinerary(ItineraryBase):
    id: int
    travel_id: int
    class Config:
        orm_mode = True
