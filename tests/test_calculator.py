from src.calculator import *
import pytest

def test_sum():
    assert Calculator.sum(1, 1) == 2
    assert Calculator.sum(3, 4) == 7

def test_subtract():
    assert Calculator.subtract(3, 3) == 0
    assert Calculator.subtract(6, 4) == 2
    assert Calculator.subtract(5, 10) == -5

def test_multiply():
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(6, 6) == 36
    assert Calculator.multiply(-4, 5) == -20

def test_divide():
    assert Calculator.divide(9, 3) == 3
    assert Calculator.divide(24, 6) == 4
    assert Calculator.divide(-10, 5) == -2

    with pytest.raises(ValueError, match="Division by 0 is not possible."):
        Calculator.divide(10, 0)
