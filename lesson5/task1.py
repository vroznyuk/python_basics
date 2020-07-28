from datetime import datetime


with open('files/task1_out.txt', 'w', encoding='utf8') as f_in:
    while True:
        user_input = input('Введите что-нибудь для записи в файл: ')
        if not user_input:
            break
        f_in.write((datetime.now()).strftime('%d.%m.%Y %H:%M:%S') + ': ' + user_input+'\n')
