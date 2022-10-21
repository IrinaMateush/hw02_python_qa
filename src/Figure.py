FIGURES = ['circle', 'rectangle', 'square', 'triangle']


class Figure:
    """Базовый класс для всех фигур"""

    def __init__(self, name, a):
        self.name = name
        self.a = a

        if a <= 0:
            raise ValueError('Оnly positive values')

        if name not in FIGURES:
            raise ValueError('It is not figure')

    @property
    def area(self):
        pass

    def add_area(self, figure):
        return self.area + figure.area
