from datetime import UTC, datetime

from .model import Expense
from .repository import ExpenseRepository
from .schema import ExpenseRequest


class ExpenseService:

    def __init__(self, repository: ExpenseRepository):
        self._repository = repository

    def get_all_expenses(self) -> list[Expense]:

        return self._repository.find_all()

    def get_expense_by_id(self, expense_id: int) -> Expense:


        expense = self._repository.find_by_id(expense_id)

        if expense is None:
            raise ValueError(f"Expense with id {expense_id} not found.")

        return expense

    def get_expenses_by_month(
        self,
        month: int,
        year: int,
    ) -> list[Expense]:

        return self._repository.find_by_month(month, year)


    def create_update_expense(self,request:ExpenseRequest)->Expense:
       if request.id:
           return self.update_expense(request.id, request)
       else:
           return self.create_expense(request)



    def create_expense(
        self,
        request: ExpenseRequest,
    ) -> Expense:

        next_id = self._generate_next_id()

        expense = Expense(
            id=next_id,
            category=request.category,
            description=request.description,
            amount=request.amount,
            expense_date=request.expense_date,
            updated_at=datetime.now(UTC),
        )

        return self._repository.save(expense)

    def update_expense(self, expense_id: int, request: ExpenseRequest, ) -> Expense:

        expense = self.get_expense_by_id(expense_id)

        updated_expense = expense.model_copy(
            update=request.model_dump(exclude_unset=True)
        )

        updated_expense.updated_at = datetime.now(UTC)

        return self._repository.update(updated_expense)

    def delete_expense(
        self,
        expense_id: int,
    ) -> None:


        deleted = self._repository.delete(expense_id)

        if not deleted:
            raise ValueError(
                f"Expense with id {expense_id} not found."
            )

    def _generate_next_id(self) -> int:
        """
        Generate the next expense id.
        """

        expenses = self._repository.find_all()

        if not expenses:
            return 1

        return max(
            expense.id
            for expense in expenses
        ) + 1