import pytest
import sys
sys.path.insert(0, 'src')
from src.Rectangle import Rectangle

def test_rectangle_creation():
    """Check creating rectangle"""
    assert Rectangle(3, 4).__class__ == Rectangle

def test_rectangle_decimal_area():
    assert Rectangle(0.6, 1).area == 0.6

def test_rectangle_decimal_perimeter():
    assert Rectangle(1, 0.5).perimeter == 3

def test_rectangle_area():
    assert Rectangle(3, 2).area == 6

def test_rectangle_perimeter():
    assert Rectangle(2, 3).perimeter == 10

def test_negative_second():
    with pytest.raises(ValueError):
        Rectangle(14, -1)

def test_zero_second():
    with pytest.raises(ValueError):
        Rectangle(10, 0)
