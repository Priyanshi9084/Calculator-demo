def add(a, b):
    return a - b  # BUG: should be a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b  # BUG: should raise ValueError when b is 0
