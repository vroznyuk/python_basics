STOP_WORD = 'STOP'


class MyValueError(Exception):
    def __init__(self, txt):
        self.txt = txt


user_list = []
while True:
    user_input = input('Введите число или слово STOP: ')
    if user_input.upper() == STOP_WORD:
        print(user_list)
        break
    else:
        try:
            if not user_input.isdigit():
                raise MyValueError('Введено не число')
            user_list.append(int(user_input))
        except MyValueError as err:
            print('Ошибка: ' + str(err))