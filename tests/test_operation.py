import pytest
from src.math_operations import add, subtract, multiply, divide, power, square

# Happy path tests
def test_add_positive():
    assert add(2, 3) == 5.0

def test_add_negative():
    assert add(-1, -2) == -3.0

def test_add_mixed():
    assert add(-5, 10) == 5.0

def test_subtract():
    assert subtract(10, 4) == 6.0

def test_subtract_negative():
    assert subtract(5, 10) == -5.0

def test_multiply():
    assert multiply(3, 4) == 12.0

def test_multiply_zero():
    assert multiply(5, 0) == 0.0

def test_divide():
    assert divide(10, 2) == 5.0

def test_power():
    assert power(2, 3) == 8.0

def test_square():
    assert square(4) == 16.0

# Edge cases
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_float_inputs():
    assert add(2.5, 3.7) == 6.2

# Parametrized tests (efficient!)
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2.0),   # add
    (8, 3, 5.0),   # subtract
    (6, 7, 42.0),  # multiply
])
def test_basic_operations(a, b, expected):
    assert add(a, b) == expected
    assert subtract(a + expected, b) == expected
    assert multiply(a, expected) == expected
