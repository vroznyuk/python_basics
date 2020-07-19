MAX_LEN = 3


def my_func(my_list:list):
    # отсортируем список по убыванию и просуммируем первые два элемента
    my_list.sort(reverse=True)
    return my_list[0] + my_list[1]


idx = 0
numbers = list()
while idx < MAX_LEN:
    while True:
        try:
            numbers.append(int(input('Введите число ' + str(idx + 1) + ': ')))
            idx += 1
            break
        except ValueError:
            print('Вы ошиблись, повторите ввод')

print('Сумма наибольших элементов: ' + str(my_func(numbers)))



