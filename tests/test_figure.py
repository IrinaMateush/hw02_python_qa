import pytest
import sys
sys.path.insert(0, 'src')
from src.Figure import Figure

def test_figure_creation():
    """Check creating figure"""
    assert Figure('circle', 3).__class__ == Figure
 
def test_empty():
    with pytest.raises(TypeError):
        Figure()

def test_not_figure():
    with pytest.raises(ValueError):
        Figure('f', 4)

def test_attributes():
    with pytest.raises(TypeError):
        Figure('circle')
        
def test_negative_number():
    with pytest.raises(ValueError):
        Figure('circle', -1)

def test_zero():
    with pytest.raises(ValueError):
        Figure('circle', 0)