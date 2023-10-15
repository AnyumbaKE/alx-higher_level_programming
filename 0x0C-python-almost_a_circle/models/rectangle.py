#!/usr/bin/python3
"""Class Rectangle that inherits from Base:"""


from models.base import Base


class Rectangle(Base):
    """Defines class rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes"""
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
