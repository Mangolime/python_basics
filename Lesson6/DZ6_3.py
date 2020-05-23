class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{float(self._income['wage']) + float(self._income['bonus'])}"


man = Position('Ivan', 'Petrov', 'Manager', '5000', '13000')
print(man.position, man._income)
print(man.get_full_name())
print(man.get_total_income())
