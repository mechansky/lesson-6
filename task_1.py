from  time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'желтый', 'зеленый']

    def running(self):
        print('Запуск светофора')
        for element in self.__color:
            print(f'Цвет светофора: {element}')
            if element == self.__color[0]:
                sleep(7)
            if element == self.__color[1]:
                sleep(2)
            if element == self.__color[2]:
                sleep(8)


a = TrafficLight()
a.running()