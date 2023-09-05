#!/usr/bin/python3
# 6-print_comb3.py

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for first_digit in range(0, 9):
    for second_digit in range(first_digit + 1, 10):
        if first_digit < 8:
            print("{}{}, ".format(first_digit, second_digit), end="")
        else:
            print("{}{}".format(first_digit, second_digit))
