class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.color + ' ' + self.name + ' едет')

    def stop(self):
        print(self.color + ' ' + self.name + ' стоит')

    def turn(self, direction):
        print(self.color + ' ' + self.name + ' повернула ' + direction)

    def show_speed(self):
        print('Скорость ' + self.name + ' ' + str(self.speed))
        return self.speed


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        current_speed = super().show_speed()
        if current_speed > 60:
            print('Внимание! Превышение скорости!')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        current_speed = super().show_speed()
        if current_speed > 40:
            print('Внимание! Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town_car = TownCar(60, 'черная', 'Audi')
town_car.go()

sport_car = SportCar(200, 'серебряный', 'Shelby')
sport_car.go()
sport_car.turn('направо')
sport_car.stop()

work_car = WorkCar(50, 'серый', 'Hyundai')
work_car.show_speed()

police_car = PoliceCar(70, 'бело-синий', 'Ford')
if police_car.is_police:
    print('И тут нагрянула полиция!')
