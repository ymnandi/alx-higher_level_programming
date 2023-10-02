#!/usr/bin/python3
"""Module 2-rectangle"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        """Retrieve width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets width"""
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets height"""
        self.__height = value

    def area(self):
        """Returns area"""
        return self.__width * self.__height
    
    def perimeter(self):
        """Returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
