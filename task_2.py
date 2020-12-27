class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f'Длина планируемой дороги: {length} м, ширина: {width} м')

    def get_mass_for_the_whole_track(self):
        mass_for_1m = float(input('Укажите массу асфальта для покрытия одного кв метра '
                                  'дороги асфальтом, толщиной в 1 см (в кг): '))
        thickness = float(input('Укажите толщину полотна (в см): '))
        print(f'Масса асфальта, необходимая для покрытия всего дорожного полотна'
              f' равна: {(self._length * self._width * mass_for_1m * thickness)/1000} тонн')


r1 = Road(20, 5000)
r1.get_mass_for_the_whole_track()


