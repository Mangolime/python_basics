class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, mass, thickness):
        return self._length * self._width * mass * thickness


r = Road(20, 5000)
print(f"Необходимая масса асфальта: {r.asphalt_mass(25, 5) / 1000} т.")
