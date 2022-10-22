import sys
sys.path.insert(0, 'src')
from Square import Square

def test_figure_creation():
    """Check creating figure"""
    assert Square(3, 3).__class__ == Square

def test_square_area():
    assert Square(1, 1).area == 1

def test_square_perimeter():
    assert Square(1, 1).perimeter == 4
