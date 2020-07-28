from time import sleep


class TrafficLight:
    __color = 'off'  # off - начальное состояние (светофор выключен)
    # элемент словаря состояний светофора - текущий_режим: (следующий_режим, длительность_сигнала)
    __states = {'off': ('red', 0), 'red': ('yellow', 7), 'yellow': ('green', 2), 'green': ('red', 10)}

    def __get_next_state(self):
        return self.__states.get(self.__color)[0]

    def running(self):
        self.__color = self.__get_next_state()
        duration = self.__states.get(self.__color)[1]
        print(self.__color)
        sleep(duration)


traffic_light = TrafficLight()
traffic_light.running()
traffic_light.running()
traffic_light.running()
