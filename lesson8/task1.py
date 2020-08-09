from datetime import date


class MyDate:
    def __init__(self, date_str):
        self.date_str = date_str
        self.day, self.month, self.year = MyDate.parse_date(self.date_str)
        MyDate.validate(self.day, self.month, self.year)

    @classmethod
    def parse_date(cls, date_str):
        """
        :param date_str: дата в формате dd-mm-yyyy - str
        :return: [dd, mm, yyyy] - list of int
        В случае некорректного формата входной строки будет выброшено исключение ValueError
        """
        try:
            return [int(val) for val in date_str.split('-')]
        except ValueError:
            raise ValueError('Некорректный формат входной строки')

    @staticmethod
    def validate(day, month, year):
        """
        :param day: день - int
        :param month: месяц - int
        :param year: год - int
        Если валидация не пройдена, то будет выброшено исключение ValueError
        """
        if not 1 <= month <= 12:
            raise ValueError('Некорректный месяц')
        else:
            # Проверка количества дней в месяце. Можно было бы, конечно, написать свой алгоритм,
            # но поскольку корректность месяца уже проверена выше, а в годе ошибок быть не может,
            # то можно просто попробовать преобразовать к дате, используя стандартные возможности языка
            try:
                date(year, month, day)
            except ValueError:
                raise ValueError('Некорректное число дней в месяце')


try:
    dt1 = MyDate('29-XX-2020')
except ValueError as err_txt:
    print('Ошибка 1: ' + str(err_txt))

try:
    dt2 = MyDate('29-13-2021')
except ValueError as err_txt:
    print('Ошибка 2: ' + str(err_txt))

try:
    dt3 = MyDate('29-02-2021')
except ValueError as err_txt:
    print('Ошибка 3: ' + str(err_txt))

try:
    dt4 = MyDate('29-02-2020')
    print('А здесь все хорошо')
except ValueError as err_txt:
    print('Ошибка 4: ' + str(err_txt))