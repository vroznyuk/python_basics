class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        dividend = float(input('Введите делимое: '))
        break
    except ValueError:
        print('Ошибка: Вы ввели не число')

while True:
    try:
        divider = float(input('Введите делитель: '))
        if divider == 0:
            raise MyZeroDivisionError('Делить на ноль нельзя')
        break
    except ValueError:
        print('Ошибка: Вы ввели не число')
    except MyZeroDivisionError as err:
        print(err)

print('Результат деления: ' + str(dividend/divider))