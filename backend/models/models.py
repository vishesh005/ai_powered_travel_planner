from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.database.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    travels = relationship("Travel", back_populates="user")

class Travel(Base):
    __tablename__ = "travels"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    destination = Column(String, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    budget = relationship("Budget", back_populates="travel", uselist=False)
    hotels = relationship("Hotel", back_populates="travel")
    itinerary = relationship("Itinerary", back_populates="travel")
    user = relationship("User", back_populates="travels")

class Budget(Base):
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True, index=True)
    travel_id = Column(Integer, ForeignKey("travels.id"))
    amount = Column(Float)
    travel = relationship("Travel", back_populates="budget")

class Hotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True, index=True)
    travel_id = Column(Integer, ForeignKey("travels.id"))
    name = Column(String)
    address = Column(String)
    price_per_night = Column(Float)
    travel = relationship("Travel", back_populates="hotels")

class Itinerary(Base):
    __tablename__ = "itineraries"
    id = Column(Integer, primary_key=True, index=True)
    travel_id = Column(Integer, ForeignKey("travels.id"))
    day = Column(Integer)
    activity = Column(String)
    travel = relationship("Travel", back_populates="itinerary")
