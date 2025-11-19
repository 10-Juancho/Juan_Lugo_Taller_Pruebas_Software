from calculator import Calculator
import pytest

def test_addition():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-2, 3) == 1
    assert calc.add(0, 0) == 0

def test_subtraction():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2
    assert calc.subtract(0, 0) == 0

def test_multiplication():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 10) == 0

def test_division():
    calc = Calculator()
    assert calc.divide(6, 2) == 3
    assert calc.divide(-6, 3) == -2

def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(5, 0)
