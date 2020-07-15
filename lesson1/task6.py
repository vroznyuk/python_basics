DAILY_COEFF = 0.1

a = float(input("Сколько километров спортсмен пробежал в первый день?"))
b = float(input("А какая у него цель в километрах?"))

dist_today = a
i = 1
while True:
    if dist_today >= b:
        print(f"Спортсмен достиг своей цели {b:0.2f} км в день №{i}")
        break

    i += 1
    dist_today = round(dist_today * (1 + DAILY_COEFF), 2)
    # print(f"{i}-й день: {dist_today:0.2f}")
