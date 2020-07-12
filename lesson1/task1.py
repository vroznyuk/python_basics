import datetime
import locale

locale.setlocale(locale.LC_ALL, "")

current_datetime = datetime.datetime.today()

print(f"Сегодня {current_datetime.strftime('%d %B %Y')} года")
print(f"На часах {current_datetime.strftime('%H:%M:%S')}")

user_name = input("Как тебя зовут?").capitalize()
print("Привет, " + user_name + "!")
user_age = input(user_name + ", сколько тебе лет?")
user_exp = input("А какой у тебя стаж в программировании?")

rest_years = int(user_age) - int(user_exp)
if rest_years < 0:
    print("Что-то не сходится...")
else:
    last_digit = rest_years % 10
    if (11 <= rest_years <= 14) or (last_digit == 0) or (5 <= last_digit <= 9):
        years_txt = "лет"
    elif last_digit == 1:
        years_txt = "год"
    else:
        years_txt = "года"
    print(f"Риторический вопрос: на что же ты потратил {rest_years} {years_txt} своей жизни?..")

