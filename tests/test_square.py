import pytest
import sys
sys.path.insert(0, 'src')
from src.Square import Square

def test_figure_creation():
    """Check creating figure"""
    assert Square('square', 3, 3).__class__ == Square

def test_square_area():
    assert Square('square', 1, 1).area == 1

def test_square_perimeter():
    assert Square('square', 1, 1).perimeter == 4
