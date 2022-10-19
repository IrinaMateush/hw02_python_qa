from Figure import Figure

class Square(Figure):
    """класс для квадрата"""  
    def __init__(self, name, a):
        super().__init__(name,a)

    @property
    def perimeter(self): 
        return self.a*4
