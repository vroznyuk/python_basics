STOP_WORD = 'STOP'

user_set = []
print('Введите поочередно любое количество элементов списка. Для окончания ввода введите STOP')
i = 1  # Счетчик введенных элементов
while True:
    new_item = input(f'Элемент {i}: ')
    if new_item == STOP_WORD:
        break
    i += 1
    user_set.append(new_item)

print('Было:', user_set)

# Меняем местами соседние элементы в паре
j = 0
while j < (len(user_set) - len(user_set) % 2):
    user_set[j], user_set[j + 1] = user_set[j + 1], user_set[j]
    j += 2

print('Стало:', user_set)
