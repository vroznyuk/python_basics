from random import randint

MAX_RANGE = 20
MIN_VAL = -100
MAX_VAL = 100


def my_range(a:int) -> int:
    idx = 0
    while idx < a:
        yield idx
        idx += 1


init_list = [randint(MIN_VAL, MAX_VAL) for _ in my_range(MAX_RANGE)]
print('Исходный список:\n' + str(init_list))

final_list = [itm for idx, itm in enumerate(init_list[1:]) if itm > init_list[idx]]
print('Вот что получилось:\n' + str(final_list))