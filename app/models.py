from pydantic import BaseModel


class Expense(BaseModel):
    id: int
    category: str
    amount: float
    month: str