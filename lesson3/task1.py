def my_div(p_dividend, p_divider):
    return p_dividend / p_divider


while True:
    try:
        dividend = float(input('Введите делимое:'))
        try:
            divider = float(input('Введите делитель:'))
            break
        except:
            print('Ошибка: Вы ввели не число')
    except ValueError:
        print('Ошибка: Вы ввели не число')

try:
    print(f'{dividend} / {divider} = ' + str(my_div(dividend, divider)))
except ZeroDivisionError:
    print('Ошибка: деление на 0 запрещено')
