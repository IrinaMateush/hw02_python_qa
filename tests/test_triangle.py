import pytest
import sys
sys.path.insert(0, 'src')

from src.Triangle import Triangle

def test_triangle_creation():
    """Check creating figure"""
    assert Triangle('triangle', 1, 1, 1).__class__ == Triangle

def test_obtuse_triangle_perimeter():
    """Check perimeter versatile and obtuse triangle"""
    assert Triangle('triangle', 4, 3, 2).perimeter == 9

def test_versatile_triangle_area():
    """Check area versatile and acute triangle"""
    assert Triangle('triangle', 6, 5, 7).area == 14

def test_versatile_triangle_perimeter():
    """Check perimeter versatile and acute triangle"""
    assert Triangle('triangle', 6, 5, 7).perimeter == 18

def test_isosceles_triangle_area():
    """Check area isosceles and right triangle"""
    assert Triangle('triangle', 3, 4, 5).area == 6

def test_isosceles_triangle_perimeter():
    """Check perimeter isosceles and right triangle"""
    assert Triangle('triangle', 3, 4, 5).perimeter == 12

def test_equilateral_triangle_area():
    """Check area equilateral triangle"""
    assert Triangle('triangle', 2, 2, 2).area == 1

def test_equilateral_triangle_perimeter():
    """Check perimeter equilateral triangle"""
    assert Triangle('triangle', 5, 5, 5).perimeter == 15

def test_negative_second():
    with pytest.raises(ValueError):
        Triangle('triangle', 14, -1, 4)

def test_zero_second():
    with pytest.raises(ValueError):
        Triangle('triangle', 10, 0, 4)

def test_negative_third():
    with pytest.raises(ValueError):
        Triangle('triangle', 14, 4, -1)

def test_zero_third():
    with pytest.raises(ValueError):
        Triangle('triangle', 10, 4, 0)