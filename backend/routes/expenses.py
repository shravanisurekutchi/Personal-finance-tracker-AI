from typing import List

from math import ceil

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import Expense
from ai.categorizer import auto_categorize

router = APIRouter()

class ExpenseCreate(BaseModel):
    title: str
    amount: float

class ExpenseOut(BaseModel):
    id: int
    title: str
    amount: float
    category: str

    class Config:
        orm_mode = True

@router.post("/add-expense", response_model=ExpenseOut)
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    category = auto_categorize(expense.title)

    db_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=category,
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


@router.get("/expenses", response_model=List[ExpenseOut])
def get_expenses(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()
    return expenses

@router.get("/insights")
def get_insights(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()
    if not expenses:
        return {
            "total_spent": 0,
            "total_transactions": 0,
            "top_category": None,
            "avg_spent": 0,
            "message": "No expenses yet. Add some to see insights!"
        }

    total_spent = sum(e.amount for e in expenses)
    total_transactions = len(expenses)

    by_category = {}
    for e in expenses:
        by_category[e.category] = by_category.get(e.category, 0) + e.amount

    top_category = max(by_category.items(), key=lambda x: x[1])[0]

    avg_spent = total_spent / total_transactions

    msg_parts = [
        f"Total spending so far: ${total_spent:.2f}.",
        f"Highest spending category: {top_category}.",
        f"Average per transaction: ${avg_spent:.2f}."
    ]

    if by_category.get("food", 0) > 0.4 * total_spent:
        msg_parts.append("You are spending a lot on food. You might try cooking at home more often.")
    if by_category.get("shopping", 0) > 0.3 * total_spent:
        msg_parts.append("Shopping is taking a big chunk of your budget. Consider pausing non-essential purchases.")
    if total_spent > 500:
        msg_parts.append("Your total spending is above $500. Setting a monthly budget may help you control costs.")

    message = " ".join(msg_parts)

    return {
        "total_spent": round(total_spent, 2),
        "total_transactions": total_transactions,
        "top_category": top_category,
        "avg_spent": round(avg_spent, 2),
        "message": message
    }