#!/usr/bin/python3


class Square:
    """Square class."""
    def __init__(self, size=0):
        """__init__ method."""
        self.__size = size

    @property
    def size(self):
        """Getter method."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """area method."""
        return self.__size ** 2

    def my_print(self):
        """my_print method."""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
