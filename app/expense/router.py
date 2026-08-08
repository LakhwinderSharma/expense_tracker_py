from fastapi import APIRouter, Depends, HTTPException, status

from .repository import ExpenseRepository
from .schema import ExpenseRequest, ExpenseResponse
from .service import ExpenseService

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"],
)


def get_expense_service() -> ExpenseService:
    repository = ExpenseRepository()
    return ExpenseService(repository)


@router.get(
    "",
    response_model=list[ExpenseResponse],
    status_code=status.HTTP_200_OK,
)
def get_all_expenses(
    service: ExpenseService = Depends(get_expense_service),
):
    """
    Get all expenses.
    """
    return service.get_all_expenses()


@router.get(
    "/{expense_id}",
    response_model=ExpenseResponse,
    status_code=status.HTTP_200_OK,
)
def get_expense_by_id(
    expense_id: int,
    service: ExpenseService = Depends(get_expense_service),
):
    """
    Get expense by id.
    """

    try:
        return service.get_expense_by_id(expense_id)

    except ValueError as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(ex),
        )


@router.get(
    "/month/{year}/{month}",
    response_model=list[ExpenseResponse],
    status_code=status.HTTP_200_OK,
)
def get_expenses_by_month(
    year: int,
    month: int,
    service: ExpenseService = Depends(get_expense_service),
):
    """
    Get expenses for a month.
    """

    return service.get_expenses_by_month(
        month=month,
        year=year,
    )


@router.post(
    "",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_expense(
    request: ExpenseRequest,
    service: ExpenseService = Depends(get_expense_service),
):
    """
    Create a new expense.
    """

    return service.create_expense(request)


@router.put(
    "/{expense_id}",
    response_model=ExpenseResponse,
)
def update_expense(
    expense_id: int,
    request: ExpenseRequest,
    service: ExpenseService = Depends(get_expense_service),
):
    """
    Update an expense.
    """

    try:
        return service.update_expense(
            expense_id,
            request,
        )

    except ValueError as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(ex),
        )


@router.delete(
    "/{expense_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_expense(
    expense_id: int,
    service: ExpenseService = Depends(get_expense_service),
):
    """
    Delete an expense.
    """

    try:
        service.delete_expense(expense_id)

    except ValueError as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(ex),
        )