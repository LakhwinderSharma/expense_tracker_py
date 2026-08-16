import json
from pathlib import Path

from .model import Expense


class ExpenseRepository:

    def __init__(self) -> None:
        self._file_path = Path(__file__).parent / "expenses.json"

    def find_all(self) -> list[Expense]:

        if not self._file_path.exists():
            return []

        with self._file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return [Expense.model_validate(item) for item in data  ]

    def find_by_id(self, expense_id: int) -> Expense | None:

        expenses = self.find_all()

        return next( (expense for expense in expenses if expense.id == expense_id), None)

    def find_by_month(self, month: int,year: int,) -> list[Expense]:


        return [
            expense
            for expense in self.find_all()
            if expense.expense_date.month == month
            and expense.expense_date.year == year
        ]

    def save(self, expense: Expense) -> Expense:


        expenses = self.find_all()

        expenses.append(expense)

        self._save_all(expenses)

        return expense

    def update(self, expense: Expense) -> Expense:

        expenses = self.find_all()

        for index, existing in enumerate(expenses):

            if existing.id == expense.id:
                expenses[index] = expense
                self._save_all(expenses)
                return expense

        raise ValueError(f"Expense {expense.id} not found.")

    def delete(self, expense_id: int) -> bool:

        expenses = self.find_all()

        filtered = [expense for expense in expenses if expense.id != expense_id ]

        if len(filtered) == len(expenses):
            return False

        self._save_all(filtered)

        return True

    def _save_all(self,expenses: list[Expense], ) -> None:

        data = [expense.model_dump(mode="json")for expense in expenses ]

        with self._file_path.open("w", encoding="utf-8",) as file: json.dump(data,file, indent=4,)