class Stationery:
    title = ''

    def __init__(self, title='Канцелярская принадлежность'):
        self.title = title

    def draw(self):
        print(self.title + ': запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        print(self.title + ' не пишет')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print(self.title + ' тупой')


class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print(self.title + ' засох')


stationery = Stationery()
stationery.draw()
pen = (Pen().draw())
pencil = (Pencil().draw())
handle = (Handle().draw())