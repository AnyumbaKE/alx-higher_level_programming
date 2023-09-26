#!/usr/bin/python3

"""Calculating Area and circumference of a circle"""

import math


class MagicClass:
    """Initialize and define methods area and circumference"""
    def __init__(self, radius=0):
        """Initialize MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate area"""
        return (math.pi * self.__radius ** 2)

    def circumference(self):
        """Calcualte circumference"""
        return (math.pi * self.__radius * 2)
