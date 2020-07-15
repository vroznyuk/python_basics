income = float(input("Укажите размер выручки: "))
cost = float(input("Укажите размер издержек: "))

if income > cost:
    print("Поздравляю, фирма работает с прибылью")

    profit = income - cost
    efficiency = round(profit / income, 2)
    print(f"Прибыль {profit}")
    print(f"Рентабельность: {efficiency}")

    employees_num = int(input("Введите численность сотрудников: "))
    income_per_employee = round(profit/employees_num, 2)
    print(f"Прибыль в расчете на одного сотрудника: {income_per_employee}")
else:
    print("Увы, фирма несет убытки")