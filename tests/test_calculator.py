from src.calculator import *

def test_sum():
    assert sum(1, 1) == 2
    assert sum(3, 4) == 7

def test_subtract():
    assert subtract(3, 3) == 0
    assert subtract(6, 4) == 2
    assert subtract(5, 10) == -5

def test_divide():
    assert divide(9, 3) == 3
    assert divide(24, 6) == 6
    assert divide(-10, 5) == -2