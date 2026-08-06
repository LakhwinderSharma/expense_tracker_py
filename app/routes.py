from fastapi import APIRouter

from .service import expense_service

router = APIRouter()


@router.get("/expenses/{month}")
def get_expenses(month: str):
    return expense_service.get_expenses_by_month(month)