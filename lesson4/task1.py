from sys import argv


def calc_salary(p_hours:float, p_rate:float, p_prize:float) -> float:
    return p_hours * p_rate + p_prize


try:
    _, hours, rate, prize, *__ = argv
except ValueError:
    print('usage: <filename.py> <hours> <rate> <prize>')

print('Заработная плата: ' + str(calc_salary(float(hours), float(rate), float(prize))))