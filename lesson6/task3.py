class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {}

    def __init__(self, name, surname, position, **income):
        """
        :param name: имя
        :param surname: фамилия
        :param position: должность
        :param income: доход
        """
        self.name = name
        self.surname = surname
        self.position = position
        for key, value in income.items():
            self._income[key] = value


class Position(Worker):
    def __init__(self, name, surname, position, **income):
        """
        :param name: имя
        :param surname: фамилия
        :param position: должность
        :param income: доход
        """
        super().__init__(name, surname, position, **income)

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


pos1 = Position('Елена', 'Петрова', 'управляющий директор', **{'wage': 150000, 'bonus': 40000})
print(pos1.position + ' ' + pos1.get_full_name() + ' имеет доход ' + str(pos1.get_total_income()))