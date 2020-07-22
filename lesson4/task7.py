def fact(n:int):
    idx = 1
    curr_val = 1
    while idx <= n:
        curr_val *= idx
        yield idx, curr_val
        idx += 1


while True:
    user_n = input('Введите число n: ')
    if user_n.isdigit():
        break
    else:
        print('Вы ошиблись, повторите ввод')

for num, el in fact(int(user_n)):
    print(f'{num}! = {el}')
