from src.calculator import *

def test_sum():
    assert sum(1, 1) == 2
    assert sum(3, 4) == 7

def test_subtract():
    assert subtract(3, 3) == 0
    assert subtract(6, 4) == 2
    assert subtract(5, 10) == -5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(6, 6) == 36
    assert multiply(-4, 5) == -20