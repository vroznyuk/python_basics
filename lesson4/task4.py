from random import randint

MIN_VAL = 10
MAX_VAL = 20
MAX_LEN = 10

init_list = [randint(MIN_VAL, MAX_VAL) for _ in range(MAX_LEN)]
print('Исходный список:\n' + str(init_list))

new_list = [itm for itm in init_list if init_list.count(itm) == 1]
print('Финальный список:\n' + str(new_list))