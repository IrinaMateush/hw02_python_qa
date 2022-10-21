import pytest
import sys
sys.path.insert(0, 'src')
from src.Circle import Circle

def test_radius_decimal():
    assert Circle('circle', 0.5).area == 1 

def test_big_radius():
    assert Circle('circle', 100).area == 31415

def test_radius_decimal():
    assert Circle('circle', 0.5).perimeter == 3

def test_big_radius():
    assert Circle('circle', 100).perimeter == 628
    