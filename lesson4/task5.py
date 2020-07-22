from functools import reduce

MIN_VAL = 100
MAX_VAL = 1000

print('Результат:')
print(reduce(lambda x, y: x * y, [itm for itm in range(MIN_VAL, MAX_VAL + 1, 2)]))
