import json

from .models import Expense


class ExpenseService:

    def get_expenses_by_month(self, month: str):

        with open("expenses.json", "r") as file:
            data = json.load(file)

        expenses = [Expense(**expense) for expense in data]

        return [
            expense
            for expense in expenses
            if expense.month.lower() == month.lower()
        ]


expense_service = ExpenseService()