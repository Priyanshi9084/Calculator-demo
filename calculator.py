import numbers

def _validate_number(value, name="value"):
    """Validate that the provided value is a number (int or float).

    Args:
        value: The value to validate.
        name: Optional name of the argument for error messages.

    Raises:
        TypeError: If ``value`` is not an instance of ``numbers.Number``.
    """
    if not isinstance(value, numbers.Number):
        raise TypeError(f"{name} must be a number, got {type(value).__name__}")


def add(a, b):
    """Return the sum of a and b.

    Both arguments must be numbers; otherwise a ``TypeError`` is raised.
    """
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a + b


def multiply(a, b):
    """Return the product of a and b.

    Both arguments must be numbers; otherwise a ``TypeError`` is raised.
    """
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a * b


def divide(a, b):
    """Return the division of a by b.

    Args:
        a: Numerator.
        b: Denominator.

    Raises:
        ValueError: If b is zero.
        TypeError: If either ``a`` or ``b`` is not a number.
    """
    _validate_number(a, "a")
    _validate_number(b, "b")
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
