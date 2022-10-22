from src.Figure import Figure
import pytest
import sys
sys.path.insert(0, 'src')


def test_figure_creation():
    """Check creating figure"""
    assert Figure(3).__class__ == Figure


def test_empty():
    with pytest.raises(TypeError):
        Figure()


def test_negative_number():
    with pytest.raises(ValueError):
        Figure(-1)


def test_zero():
    with pytest.raises(ValueError):
        Figure(0)
