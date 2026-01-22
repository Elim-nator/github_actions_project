def add(a, b):
    """Returns sum of two numbers."""
    return float(a) + float(b)

def subtract(a, b):
    """Returns a minus b."""
    return float(a) - float(b)

def multiply(a, b):
    """Returns product of two numbers."""
    return float(a) * float(b)

def divide(a, b):
    """Returns a divided by b. Raises ValueError if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return float(a) / float(b)

def power(a, b):
    """Returns a raised to power b."""
    return float(a) ** float(b)

def square(number):
    """Returns square of a number."""
    return multiply(number, number)
