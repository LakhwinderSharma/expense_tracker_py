import json
from pathlib import  Path
from .model import Income
class IncomeRepository:

    def __init__(self)-> None:
        self._file_Path = Path(__file__).parent / "income.json"

    def find_incomes(self) ->list[Income]:
        if not self._file_Path.exists():
            return []

        with self._file_Path.open('r',encoding="utf-8") as file :
            data = json.load(file)

        incomes = []
        for item in data:
            income = Income.model_validate(item)
            incomes.append(income)
        return incomes

    def find_income_by_id(self, income_id:int) ->Income | None:
        incomes = self.find_incomes()
        return next ((income for income in incomes if income.id ==income_id), None)

    def save(self,income: Income) -> Income:
        incomes = self.find_incomes()
        incomes.append(income)
        self.save_all(incomes)
        return income

    def save_all(self, incomes: list[Income])->None:

        data =[income.model_dump(mode="json") for income in incomes]

        with self._file_Path.open("w", encoding="utf-8",) as file:
            json.dump(data,file,indent=4)


    def update(self, income: Income) -> Income:

        incomes = self.find_incomes()

        for index, existing in enumerate(incomes):

            if existing.id == income.id:
                incomes[index] = income
                self.save_all(incomes)
                return income

        raise ValueError(f"Expense {income.id} not found.")

    def delete(self, income_id: int) -> bool:

        incomes = self.find_incomes()

        filtered = [income for income in incomes if income.id != income_id ]

        if len(filtered) == len(incomes):
            return False

        self.save_all(filtered)

        return True

