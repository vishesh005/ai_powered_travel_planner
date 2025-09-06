from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.schemas import Budget, BudgetCreate
from backend.crud.crud import create_budget, get_budget
from backend.database.database import SessionLocal

router = APIRouter(prefix="/budgets", tags=["budgets"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Budget)
def create_new_budget(budget: BudgetCreate, db: Session = Depends(get_db)):
    return create_budget(db, budget)

@router.get("/{budget_id}", response_model=Budget)
def read_budget(budget_id: int, db: Session = Depends(get_db)):
    db_budget = get_budget(db, budget_id)
    if db_budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    return db_budget
