from functools import reduce
from random import random

MAX_COUNT = 10

with open('files/task5_out.txt', 'w+', encoding='utf8') as f_obj:
    for itm in (round(random() * 100, 2) for _ in range(MAX_COUNT)):
        f_obj.write(str(itm) + ' ')

    f_obj.seek(0)
    my_list = [float(itm) for itm in f_obj.readline().split(' ') if itm != '']
    print('Сумма чисел ' + str(reduce(lambda x, y: x + y, my_list)))
