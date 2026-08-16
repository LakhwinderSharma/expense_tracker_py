from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, status

from .repository import IncomeRepository
from app.income.service import IncomeService
from .schema import IncomeResponse,IncomeRequest

router = APIRouter( prefix ="/income",tags=["Income"])

def get_income_service() ->IncomeService:
    repository = IncomeRepository()
    return IncomeService(repository)


@router.get(path="", response_model=list[IncomeResponse], status_code=status.HTTP_200_OK)
def get_all_incomes(service : IncomeService =Depends(get_income_service)):
    return service.get_all_incomes()


@router.post(path="", response_model=IncomeResponse, status_code=status.HTTP_200_OK)
def create_update_income(request: IncomeRequest,service :IncomeService =Depends(get_income_service)):
    return service.create_update_income(request)
