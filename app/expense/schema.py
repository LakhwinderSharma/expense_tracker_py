
from pydantic import BaseModel, ConfigDict,Field
from decimal import Decimal
from datetime import date, datetime


class ExpenseRequest(BaseModel):

    model_config = ConfigDict(extra='forbid',validate_assignment=True,str_strip_whitespace=True,)

    id: int
    category: str = Field(...,min_length=2,max_length=50,)
    description: str
    amount: Decimal = Field(..., gt=0,decimal_places=2,)
    expense_date: date


class ExpenseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    category: str
    description: str
    amount: Decimal
    expense_date: date