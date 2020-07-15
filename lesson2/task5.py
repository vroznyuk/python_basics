STOP_WORD = 'STOP'

rating = [28, 27, 23, 15, 14, 14, 11]
print('Исходный рейтинг:', rating, '\n')

while True:
    user_input = input(f'Введите число или слово {STOP_WORD}: ')
    if user_input.upper() == STOP_WORD:
        break

    if user_input.isdigit():
        new_value = int(user_input)
        i = 0  # счетчик элементов списка
        while i < len(rating):
            if new_value > rating[i]:
                rating.insert(i, new_value)
                break
            i += 1
        else:
            rating.append(new_value)

        print('Текущий рейтинг:', rating, '\n')
    else:
        print('Вы ввели не число, попробуйте еще раз')
