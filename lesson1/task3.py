MAX_DIGITS = 3

n = int(input("Введите n: "))

sum = 0
i = 0
output_txt = ""
nn = 0
while i < MAX_DIGITS:
    nn += n * (10 ** i)
    sum += nn
    if not output_txt:
        output_txt = output_txt + str(nn)
    else:
        output_txt = output_txt + " + " + str(nn)

    i += 1

print("Результат: " + output_txt + " = " + str(sum))