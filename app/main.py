from fastapi import FastAPI

from .routes import router

app = FastAPI(title="Expense Tracker")

app.include_router(router)