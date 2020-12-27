class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if is_police:
            print(f'автомобиль {name} {color} является полицейским!')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} {self.color} составляет {self.speed} км/час')

    def go(self):
        print(f'Автомобиль {self.name} {self.color} поехал')

    def stop(self):
        print(f'Автомобиль {self.name} {self.color} остановился\n')

    def turn(self, direction):
        print(f'Автомобиль поехал в направлении: {direction}')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля {self.name} {self.color} составляет {self.speed} км/час')
        if self.speed > 60:
            print(f'Внмиание! У автомобиля превышение скорости! Ограничение для городского автомобиля 60 км/час')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля {self.name} {self.color} составляет {self.speed} км/час')
        if self.speed > 40:
            print(f'Внмиание! У автомобиля превышение скорости! Ограничение для рабочего автомобиля 40 км/час')


class PoliceCar(Car):
    pass


print('начало тут\n ')

car1 = TownCar(80, 'Black', 'Volvo', False)
car2 = SportCar(120, 'Red', 'Ferrari', False)
car3 = WorkCar(45, 'White', 'Mercedes', False)
car4 = PoliceCar(150, 'Black and white', 'Ford', True)

l = [car1, car2, car3, car4]

for element in l:
    element.go()
    element.turn('направо')
    element.show_speed()
    element.stop()




