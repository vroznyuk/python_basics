from itertools import count, cycle
from random import randint

MAX_ITER = 10

start_val = randint(5, 10)
print(f'Генерация {MAX_ITER} целых чисел, начиная с {start_val}:')
for itm in count(start_val):
    if itm - start_val < MAX_ITER:
        print(itm)
    else:
        break

# Код на следующей строке не работает. Почему - пока не поняла
# print([itm for itm in count(start_val) if itm - start_val < MAX_ITER])

idx = 0
my_list = 'repeatme'
print(f'Цикл по символам строки "{my_list}" - {len(my_list)*len(my_list)} итерации:')
for itm in cycle(my_list):
    if idx < len(my_list) * len(my_list):
        print(itm, end='')
        if not ((idx + 1) % len(my_list)):
            print('')
        idx += 1
    else:
        break



