#!/usr/bin/python3
"""Module 7-rectangle"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        """Retrieve width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area"""
        return self.__width * self.__height
    
    def perimeter(self):
        """Returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
    
    def __str__(self):
        """Returns string representation"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return ((str(self.print_symbol) * self.__width + "\n") * self.__height)[:-1]
    
    def __repr__(self):
        """Returns formal string representation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
    
    def __del__(self):
        """Prints message when instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
