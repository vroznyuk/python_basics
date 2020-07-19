STOP_SYM = '#'


def my_sum(lst:list):
    result = 0
    for itm in lst:
        result += itm

    return result


def del_spaces(string:str):  # удаление лишних пробелов
    result = ''
    idx = 0
    prev_space = True
    try:
        while idx < len(string):
            if string[idx] == ' ' and not prev_space:
                result += string[idx]
                prev_space = True
            elif string[idx] != ' ':
                result += string[idx]
                prev_space = False
            idx += 1

        if result[-1] == ' ':
            result = result[:-1]
    except IndexError:
        pass

    return result


is_finished = False
total_sum = 0
while not is_finished:
    user_input = input('Введите числа через пробел и/или символ ' + STOP_SYM + ' для завершения:\n')
    try:
        if user_input.find(STOP_SYM) >= 0:
            is_finished = True

        clear_str = del_spaces(user_input.replace(STOP_SYM, ''))  # удаляем STOP_SYM и лишние пробелы из строки
        if clear_str != '':
            total_sum += my_sum([int(num) for num in clear_str.split(' ')])
            print(f'Общая сумма: {total_sum}')
    except ValueError:
        # не нашли STOP_SYM
        print('Ошибка: некорректное число. Повторите ввод')
        is_finished = False

