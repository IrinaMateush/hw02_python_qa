class Figure:
    """Базовый класс для всех фигур"""

    def __init__(self, a):
        self.a = a

        if a <= 0:
            raise ValueError('Оnly positive values')

    @property
    def area(self):
        pass

    def add_area(self, figure):
        if isinstance(figure, Figure) == False:
            raise ValueError('It is not figure')
        return self.area + figure.area
