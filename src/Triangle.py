import math

from Figure import Figure


class Triangle(Figure):
    """класс для треугольника"""

    def __init__(self, name, a, b, c):
        super().__init__(name, a)
        self.b = b
        self.c = c

        if b <= 0:
            raise ValueError('Оnly positive values')

        if c <= 0:
            raise ValueError('Оnly positive values')

        if (self.a + self.b) < self.c:
            raise ValueError('It is not triangle')

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = int(self.perimeter / 2)
        return math.isqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

cc = Triangle('triangle', 1, 1, 1)

