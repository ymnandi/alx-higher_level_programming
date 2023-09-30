#!/usr/bin/python3
""" Module that defines a function that adds 2 integers."""


def add_integer(a, b=98):
    """Function that adds 2 integers.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The return value. The sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
