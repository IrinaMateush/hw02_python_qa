from Square import Square

class Rectangle(Square):
    """класс для прямоугольника"""  
    def __init__(self, name, a, b):
        super().__init__(name, a)
        self.b = b

    @property
    def perimeter(self):
        return (self.a + self.b)*2

    @property
    def area(self): 
        return self.a*self.b