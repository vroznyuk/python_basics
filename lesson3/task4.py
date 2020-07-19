def my_pow_v1(x:float, y:int):
    if y < 0:
        return 1 / x ** (y * (-1))
    else:
        return x ** y


def my_pow_v2(x:float, y:int):
    var_y = y
    if y < 0:
        var_y = y * (-1)

    idx = 1
    result = 1
    while idx <= var_y:
        result *= x
        idx += 1

    if y < 0:
        result = 1 / result

    return result


while True:
    try:
        user_x = float(input('Введите x: '))
        break
    except ValueError:
        print('Это не действительное число, попробуйте еще раз')

while True:
    try:
        user_y = int(input('Введите y: '))
        break
    except ValueError:
        print('Это не целое число, попробуйте еще раз')

print('Первым способом получилось x ^ y = ' + str(my_pow_v1(user_x, user_y)))
print('Вторым способом получилось x ^ y = ' + str(my_pow_v2(user_x, user_y)))
