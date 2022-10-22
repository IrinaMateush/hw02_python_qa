from Figure import Figure


class Rectangle(Figure):
    """класс для прямоугольника"""

    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

        if b <= 0:
            raise ValueError('Оnly positive values')

    @property
    def perimeter(self):
        return (self.a + self.b) * 2

    @property
    def area(self):
        return self.a * self.b
