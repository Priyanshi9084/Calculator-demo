def add(a, b):
    """Return the sum of a and b.

    The original implementation mistakenly performed subtraction, which caused the
    `test_add` unit test to fail. The correct behavior is to add the two numbers.
    """
    return a + b


def multiply(a, b):
    """Return the product of a and b.

    This function was already correct.
    """
    return a * b


def divide(a, b):
    """Return the division of a by b.

    The original implementation divided without handling division‑by‑zero. The
    tests expect a ``ValueError`` to be raised when ``b`` is zero, so we add an
    explicit check before performing the division.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
