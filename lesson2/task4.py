while True:
    my_set = input('Напиши осмысленное предложение:\n').split(' ')
    if len(my_set) > 1:
        break
    else:
        print('Ну давай хотя бы из двух слов, ок?')

print('=== Вывод нумерованного списка ===')
for idx, itm in enumerate(my_set):
    print(idx, itm[0:10])