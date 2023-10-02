#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
"""


class Rectangle:
    """
    Represents class rectangle

    Args:
        width (int): width
        height (int): height
    """
    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
