while True:
    month_number = input('Введите порядковый номер месяца: ')
    if month_number.isdigit() and 1 <= int(month_number) <= 12:
        month_number = int(month_number)
        break
    else:
        print('Попробуйте еще раз, просто число от 1 до 12')

print('=== Релизация с помощью списков ===')
lst_months = [[1, 2, 12], [3, 4, 5], [6, 7, 9], [9, 10, 11]]  # номера месяцев сгруппированы по временам года
lst_seasons = ['зима', 'весна', 'лето', 'осень']

for itm in lst_months:
    if month_number in itm:
        print(f'Время года - {lst_seasons[lst_months.index(itm)]}')
        break

print('=== Релизация с помощью словаря ===')

dict_seasons = {
    (1, 2, 12): 'зима',
    (3, 4, 5): 'весна',
    (6, 7, 8): 'лето',
    (9, 10, 11): 'осень'
}

# Если есть более изящное решение, как обработать ключ-кортеж, то буду очень благодарна за совет
for itm in dict_seasons:
    if month_number in itm:
        print(f'Время года - {dict_seasons.get(itm)}')
        break
