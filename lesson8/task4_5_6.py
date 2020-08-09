# Атрибуты классов, конечно, высосаны из пальца
class OfficeEquipmentException(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:  # Оргтехника
    def __init__(self, model: str, name_equipment: str):
        """
        :param model: модель
        :param name_equipment: название устройства
        """
        self.name_equipment = name_equipment
        self.model = model


class Printer(OfficeEquipment):  # Принтер
    def __init__(self, model: str, kind: str, is_colored: bool):
        """
        :param model: модель
        :param kind: тип принтера (струйный, лазерный)
        :param is_colored: True - цветной, False - черно-белый
        """
        super().__init__(model, 'Принтер')
        self.kind = kind
        self.is_colored = is_colored


class Scanner(OfficeEquipment):  # Сканер
    def __init__(self, model: str, kind: str):
        """
        :param model: модель
        :param kind: тип сканера (планшетный, протяжной, планетарный)
        """
        super().__init__(model, 'Сканер')
        self.kind = kind


class XeroxMachine(OfficeEquipment):  # Ксерокс
    def __init__(self, model: str, is_colored: bool):
        """
        :param model: модель
        :param is_colored: True - цветной, False - черно-белый
        """
        super().__init__(model, 'Ксерокс')
        self.type = type
        self.is_colored = is_colored


class Storage:  # Склад
    def __init__(self):
        self.storage_record = {}  # записи о хранимой технике {наименование+модель: количество}
        self.unit_in_division = {}  # записи о выданной технике {подразделение: {наименование+модель: количество}}

    def accept_to_storage(self, equipment: OfficeEquipment, quantity: int):  # Поместить технику на склад
        """
        :param equipment: объект класса Оргтехника
        :param quantity: количество единиц
        """
        if quantity <= 0:
            raise OfficeEquipmentException('Количество должно быть больше нуля')

        key = equipment.name_equipment + ' ' + equipment.model
        # добавляется запись о новой модели оргтехники
        self.storage_record.update(
            {key: quantity if self.storage_record.get(key) is None else (self.storage_record.get(key) + quantity)})

    def move_to_division(self, equipment: OfficeEquipment, quantity: int,
                         division_name: str):  # Выдать технику со склада в подразделение
        """
        :param equipment: объект класса Оргтехника
        :param quantity: количество единиц
        :param division_name: название подразделения
        """
        if quantity <= 0:
            raise OfficeEquipmentException('Количество должно быть больше нуля')

        key = equipment.name_equipment + ' ' + equipment.model
        # проверить, есть на на складе такая техника в достаточном количестве
        if self.storage_record.get(key) is None:
            raise OfficeEquipmentException('На складе отсутствует ' + key)
        elif self.storage_record.get(key) < quantity:
            raise OfficeEquipmentException('На складе недостаточно единиц ' + key)

        # передаем технику в подразделение
        if self.unit_in_division.get(division_name) is None:
            self.unit_in_division.update({division_name: {key: quantity}})
        else:
            # пока не удалось освоить грамотный перенос строк
            units = {key: quantity if (self.unit_in_division.get(division_name)).get(key) is None else (self.unit_in_division.get(division_name)).get(key) + quantity}
            self.unit_in_division.get(division_name).update(units)

        # уменьшаем количество на складе
        self.storage_record.update(
            {key: self.storage_record.get(key) - quantity})


printer = Printer('HP M602', 'лазерный', False)
scanner = Scanner('Epson M1000', 'планшетный')
xerox = XeroxMachine('Xerox SC7005', True)

storage = Storage()
# закупили технику на склад
storage.accept_to_storage(printer, 10)
storage.accept_to_storage(scanner, 7)
storage.accept_to_storage(xerox, 2)
print('На складе было:')
print(storage.storage_record)

# передали часть в подразделения
try:
    storage.move_to_division(printer, 2, 'Бухгалтерия')
    storage.move_to_division(scanner, 1, 'Бухгалтерия')
    storage.move_to_division(xerox, 1, 'Секретариат')
    print('На складе стало:')
    print(storage.storage_record)

    print('В подразделениях стало:')
    print(storage.unit_in_division)
except OfficeEquipmentException as err:
    print('Ошибка: ' + str(err))

try:
    storage.move_to_division(scanner, 100, 'Бухгалтерия')
except OfficeEquipmentException as err:
    print('Ошибка: ' + str(err))


