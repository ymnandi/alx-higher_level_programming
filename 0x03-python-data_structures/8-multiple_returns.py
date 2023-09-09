#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character"""
    if sentence is None or sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
