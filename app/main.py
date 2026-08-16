from fastapi import FastAPI,Depends

from app.expense.router import router as expense_router
from app.income.router import router as income_router
from app.auth import authenticate
app = FastAPI(title="Expense Tracker")

app.include_router(expense_router,dependencies=[Depends(authenticate)])
app.include_router(income_router,dependencies=[Depends(authenticate)])