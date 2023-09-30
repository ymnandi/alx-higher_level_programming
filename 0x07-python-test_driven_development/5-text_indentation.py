#!/usr/bin/python3
"""Module that defines a function that prints a text with 2 new lines after
each of these characters: ., ? and :.
"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after each of these
    characters: ., ? and :.

    Args:
        text (str): Text to print.

    Returns:
        None.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n")
            if i != len(text) - 1 and text[i + 1] == " ":
                i += 1
        elif text[i] == " ":
            if i != len(text) - 1 and (text[i + 1] == "." or text[i + 1] == "?" or text[i + 1] == ":"):
                i += 1
            else:
                print("\n")
