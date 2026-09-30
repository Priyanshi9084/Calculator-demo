def add(a, b):
    """Return the sum of a and b."""
    return a + b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the division of a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    result = a / b
    # Return int if the result is an integer value to preserve expected type
    try:
        if result.is_integer():
            return int(result)
    except AttributeError:
        # result may not have is_integer (e.g., Decimal), fallback to simple check
        if isinstance(result, (int, float)) and result == int(result):
            return int(result)
    return result
