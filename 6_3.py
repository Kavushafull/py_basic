class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return f'Сотрудник {self.surname} {self.name}'
    def get_total_income(self):
        return f'Доход сотрудника {self._income.get("wage") + self._income.get("bonus")}'

a = Position('Дмитрий', 'Серов', 'инженер', {"wage": 90000, "bonus": 20000})
print(a.get_full_name())
print(a.get_total_income())
