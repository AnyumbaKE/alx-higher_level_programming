#!/usr/bin/python3
"""Class Rectangle that inherits from Base:"""


from models.base import Base


class Rectangle(Base):
    """Defines class rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
