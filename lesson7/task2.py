from abc import ABC, abstractmethod


# Абстрактный класс "Одежда"
class Clothing(ABC):
    name = ''

    @abstractmethod
    def how_many_fabric(self):
        pass


# Класс "Пальто"
class Coat(Clothing):
    def __init__(self, name: str, size: int):
        """
        :param name: название (модель) пальто - str
        :param size: размер - int
        """
        self.name = name
        self.size = size

    @property
    def how_many_fabric(self):
        return round(self.size / 6.5 + 0.5, 2)


# Класс "Костюм"
class Suit(Clothing):
    def __init__(self, name: str, height: float):
        """
        :param name:  название (модель) костюма - str
        :param height: рост в метрах - float
        """
        self.name = name
        self.height = height

    @property
    def how_many_fabric(self):
        return round(2 * self.height + 0.3, 2)


print('На пальто потребуется ' + str(Coat('Пальто', 50).how_many_fabric) + ' ед. ткани')
print('На костюм потребуется ' + str(Suit('Костюм', 1.7).how_many_fabric) + ' ед. ткани')


