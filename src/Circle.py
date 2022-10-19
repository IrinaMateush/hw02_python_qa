import math

from Figure import Figure


class Circle(Figure):
    """класс для круга"""

    def __init__(self, name, radius):
        super().__init__(name, radius)
        self.radius = radius

    @property
    def perimeter(self):
        return int(2 * math.pi * self.radius)

    @property
    def area(self):
        return int(self.radius**2 * math.pi)


dd = Circle('ectangle', 5)
print(dd.perimeter)
print(dd.area)
