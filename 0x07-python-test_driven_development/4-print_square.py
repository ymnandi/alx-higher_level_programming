#!/usr/bin/python3
"""Module that defines a function that prints a square with the character #.
"""


def print_square(size):
    """Function that prints a square with the character #.

    Args:
        size (int): Size of the square.

    Returns:
        None.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for row in range(size):
            for column in range(size):
                print("#", end="")
            print()
