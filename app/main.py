from fastapi import FastAPI

from app.expense.router import router

app = FastAPI(title="Expense Tracker")

app.include_router(router)