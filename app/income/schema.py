
from pydantic import BaseModel,Field,ConfigDict
from decimal import Decimal
from datetime import date,datetime

class IncomeRequest(BaseModel):

    model_config = ConfigDict(extra='forbid',validate_assignment=True,str_strip_whitespace=True)

    id: int | None = None
    category: str = Field(...)
    amount: Decimal = Field(..., gt=0)
    description: str
    income_date: date = Field(...)



class IncomeResponse (BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    category: str
    amount: Decimal
    description: str
    income_date: date
    updated_at: datetime
