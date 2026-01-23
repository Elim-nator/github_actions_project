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
@pytest.mark.parametrize("a, b, expected_add, expected_sub, expected_mul", [
    (1, 1, 2.0, 0.0, 1.0),    # add=2, sub=0, mul=1
    (8, 3, 11.0, 5.0, 24.0),  # add=11, sub=5, mul=24
    (6, 7, 13.0, -1.0, 42.0), # add=13, sub=-1, mul=42
])
def test_basic_operations(a, b, expected_add, expected_sub, expected_mul):
    """Test add, subtract, multiply with same inputs."""
    assert add(a, b) == expected_add
    assert subtract(a, b) == expected_sub
    assert multiply(a, b) == expected_mul
