class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        """
        :param length: длина участка дороги
        :param width: ширина участка дороги
        """
        self._length = length
        self._width = width

    def calculate_mass(self, mass_per_squared_meter, thickness):
        """
        :param mass_per_squared_meter: масса асфальта на 1 кв. м толщиной 1 cм
        :param thickness: толщина слоя асфальта (см)
        """
        return round(self._length * self._width * mass_per_squared_meter * thickness / 1000, 2)


input_dict = {
    'Ширина': ('ширину участка', 'м', float),
    'Длина': ('длину участка', 'м', float),
    'Масса на 1 кв. м': ('массу асфальта на 1 кв. м', 'кг', float),
    'Толщина': ('толщину слоя', 'см', float)
    }

user_input = {}
for key, value in input_dict.items():
    while True:
        try:
            user_input[key] = value[2](input('Укажите ' + value[0] + ', ' + value[1] + ': '))
            break
        except ValueError:
            print('Вы ошиблись, повторите ввод')

road = Road(user_input.get('Ширина'), user_input.get('Длина'))
total_mass = road.calculate_mass(user_input.get('Масса на 1 кв. м'), user_input.get('Толщина'))
print(f'Понадобится {total_mass} тонн асфальта')
