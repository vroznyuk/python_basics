OFFSET = 32 # смещение строчных и заглавных латинских букв по таблице ASCII


def int_func(word:str):
    return chr(ord(word[0]) - OFFSET) + word[1:]


def my_capitalize(string:str):
    result = ''
    for word in string.split():
        if result != '':
            result += ' '
        result += int_func(word)
    return result


while True:
    user_input = input('Введите слово строчными латинскими буквами: ')
    if not (97 <= ord(user_input[0]) <= 122):
        print('Что-то не то Вы ввели, давайте еще раз')
    else:
        break

print('Вот что получилось: ' + int_func(user_input))

user_input = input('Введите строку из нескольких слов: ')
print('Вот что получилось: ' + my_capitalize(user_input))

