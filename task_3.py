class Worker:
    total = 1

    def __init__(self, name, surname, position):
        wage = float(input(f'введите оклад сотрудника {Worker.total}: '))
        bonus = float(input(f'введите бонус сотрудника {Worker.total}: '))
        data = {
            'wage': wage,
            'bonus': bonus
        }
        self.name = name
        self.surname = surname
        self.position = position
        self._income = sum(data.values())
        Worker.total += 1


class Position(Worker):

    def get_full_name(self):
        print(f'Имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'доход сотрудника {self.name} {self.surname}: {self._income} руб')


worker1 = Position('Ivan', 'Petrov', 'Sales Manager')
worker2 = Position('Petr', 'Sidorov', 'Accountant')
worker3 = Position('Nikolay', 'Ivanov', 'Lawyer')

worker1.get_full_name()
worker1.get_total_income()
worker2.get_full_name()
worker2.get_total_income()
worker3.get_full_name()
worker3.get_total_income()



