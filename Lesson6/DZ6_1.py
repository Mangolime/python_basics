class TrafficLight:

    def __init__(self):
        self.__color = ''

    def running(self):
        from time import sleep
        from itertools import cycle
        schedule = (('красный', 7), ('желтый', 2), ('зеленый', 5))
        for t in cycle((0, 1, 2)):
            self.__color = schedule[t][0]  # Изменение сигнала светофора
            print(self.__color)  # Вывод текущего сигнала
            sleep(schedule[t][1])  # Задержка на нужное количество секунд
        return


tr_light = TrafficLight()
tr_light.running()