
from .repository import IncomeRepository
from .model import Income
from .schema import IncomeRequest,IncomeResponse
from datetime import  datetime,UTC
class IncomeService:

    def __init__(self, repository: IncomeRepository):
        self._repository=repository

    def get_all_incomes(self)-> list[Income]:
        return self._repository.find_incomes()

    def _generate_next_id(self) -> int:

        incomes = self._repository.find_incomes()

        if not incomes:
            return 1

        return max(
            income.id
            for income in incomes
        ) + 1

    def create_update_income(self, income_request: IncomeRequest)->Income:
        if income_request.id:
            return self.update_income(income_request)
        else:
            return self.create_income(income_request)

    def create_income(self, income_request: IncomeRequest) ->Income:
        next_id = self._generate_next_id()
        print(next_id)
        income = Income(id =next_id,
                         category=income_request.category,
                         amount=income_request.amount,
                         description=income_request.description,
                         income_date=income_request.income_date,
                         updated_at=datetime.now(UTC)
                        )
        return self._repository.save(income)

    def get_income_by_id(self, income_id: int) -> Income:


        income = self._repository.find_income_by_id(income_id)

        if income is None:
            raise ValueError(f"Income with id {income_id} not found.")

        return income

    def update_income(self, income_request: IncomeRequest)-> Income:
        income = self.get_income_by_id(income_request.id)
        updated_income = income.model_copy(update = income_request.model_dump(exclude_unset=True))
        updated_income.updated_at =datetime.now(UTC)
        return self._repository.update(updated_income)


