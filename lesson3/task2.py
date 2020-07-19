info_tmpl = {
    'Имя': ('имя:', str),
    'Фамилия': ('фамилию:', str),
    'Год рождения': ('год рождения:', int),
    'Город': ('город проживания:', str),
    'E-mail': ('e-mail:', str),
    'Телефон': ('телефон:', str)
    }


def user_info_to_string(**kwargs):
    result = ''
    for key, value in kwargs.items():
        if result != '':
            result += '; '
        result += key + ': ' + str(value)
    return result


info_dict = {}
for tmpl_key, tmpl_val in info_tmpl.items():
    while True:
        try:
            info_dict[tmpl_key] = tmpl_val[1](input('Введите ' + tmpl_val[0]))
            break
        except ValueError:
            print('Вы ошиблись, повторите ввод')

print(user_info_to_string(**info_dict))
