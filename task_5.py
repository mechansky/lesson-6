class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title, type, color, brand):
        super().__init__(title)
        self.type = type
        self.color = color
        self.brand = brand

    def draw(self):
        print(f'Запуск отрисовки {self.title}')
        print(f'Тип: {self.type} , цвет: {self.color}, марка "{self.brand}"\n')


class Pencil(Stationery):
    def __init__(self, title, thickness, color, brand):
        super().__init__(title)
        self.thickness = thickness
        self.color = color
        self.brand = brand

    def draw(self):
        print(f'Запуск отрисовки {self.title}')
        print(f'Толщина: {self.thickness}, цвет: {self.color}, марка "{self.brand}"\n')


class Handle(Stationery):
    def __init__(self, title, type, color, brand):
        super().__init__(title)
        self.type = type
        self.color = color
        self.brand = brand

    def draw(self):
        print(f'Запуск отрисовки {self.title}')
        print(f'Цвет: {self.color}, тип: {self.type}, марка "{self.brand}"\n')


product_1 = Pen('Ручка', 'гелевая', 'синий', 'Brauberg')
product_1.draw()

product_2 = Pencil('Карандаш', 'HB', 'черный', 'Cooh-I-Nor')
product_2.draw()

product_3 = Handle('Маркер', 'перманентный', 'красный', 'Erich Crause')
product_3.draw()