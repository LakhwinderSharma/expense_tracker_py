from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal
from datetime import date,datetime

class Income(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid',
        str_strip_whitespace=True)

    id: int = Field(...,gt=0)
    category: str = Field(...)
    amount : Decimal = Field(...,gt=0)
    description: str
    income_date: date
    updated_at:  datetime = Field(default_factory=datetime.utcnow)

