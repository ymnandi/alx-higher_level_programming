#!/usr/bin/python3
# 9-print_last_digit.py

"""Print the last digit of a number."""
def print_last_digit(number):
    """Print the last digit of a number."""
    last_digit = number % 10
    print(last_digit, end="")
    return last_digit