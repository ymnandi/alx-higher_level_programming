#!/usr/bin/python3
# 100-print_tebahpla.py

for letter in range(122, 96, -1):
    if letter % 2 != 0:
        letter = letter - 32
    print("{}".format(chr(letter)), end="")
