from fastapi import FastAPI

from app.expense.router import router as expense_router
from app.income.router import router as income_router

app = FastAPI(title="Expense Tracker")

app.include_router(expense_router)
app.include_router(income_router)