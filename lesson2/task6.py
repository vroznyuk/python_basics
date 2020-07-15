STOP_WORD = 'STOP'
DK_NAME = 'название'
DK_PRICE = 'цена'
DK_QNT = 'количество'
DK_UNIT = 'ед'

products = []

print('Сначала заполним перечень товаров')
i = 0  # счетчик товаров
while True:
    prod_name = input('Введите наименование товара или STOP для завершения ввода: ')
    if prod_name.upper() == STOP_WORD:
        break
    # тут можно проверить, введен ли уже товар с таким же названием

    while True:
        try:
            prod_price = float(input('Введите цену товара: '))
            break
        except ValueError:
            print('Ошибка! Вы ввели не число')

    while True:
        try:
            prod_qnt = int(input('Введите количество товара: '))
            if prod_qnt < 0:
                print('Ошибка! Вы ввели отрицательное число')
            else:
                break
        except ValueError:
            print('Ошибка! Вы ввели не целое число')

    prod_unit = input('Введите единицу измерения товара: ')

    products.append((i + 1, {DK_NAME: prod_name.capitalize(), DK_PRICE: prod_price, DK_QNT: prod_qnt, DK_UNIT: prod_unit.lower()}))
    i += 1

print('\nВот что получилось:')
for itm in products:
    print(itm)

print('\nТеперь сделаем аналитику')
analytics = {}
# получаем список ключей из словаря первого элемента списка (считаем, что он везде одинаковый)
key_list = list(products[0][1].keys())
for key in key_list:
    values_list = []
    for prd in products:
        values_list.append(prd[1].get(key))

    if key == DK_UNIT:  # для единиц измерения оставим только уникальные значения
        values_list = list(set(values_list))

    analytics[key] = values_list

for key, value in analytics.items():
    print(f'{key:<10}: {value}')
