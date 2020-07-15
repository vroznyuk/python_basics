n = int(input("Введите целое положительное число: "))

max_digit = n % 10
n = n // 10
while n > 0:
    if max_digit < n % 10:
        max_digit = n % 10
    n = n // 10

print(f"Наибольшая цифра в числе: {max_digit}")