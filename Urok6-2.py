class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def calc_mass(self, a, b):
        print(f"Масса асфальта, необходимая для покрытия участка дороги:{self._length * self._width * a * b}")
road = Road(5, 100)
road.calc_mass(5, 1)
