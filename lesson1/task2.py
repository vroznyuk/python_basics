num_seconds = int(input("Введите число секунд: "))

hours = num_seconds // (60 * 60)
minutes = num_seconds % (60 * 60) // 60
seconds = num_seconds % 60
print(f"В формате чч:мм:сс получается {hours}:{minutes:02d}:{seconds:02d}")
