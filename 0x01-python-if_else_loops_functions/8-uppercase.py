#!/usr/bin/python3
# 8-uppercase.py


def uppercase(str):
    """Print a string in uppercase, followed by a new line."""

    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")
