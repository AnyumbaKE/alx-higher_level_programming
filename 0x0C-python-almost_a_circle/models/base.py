#!/usr/bin/python3
"""Class Base"""

import json
import csv


class Base():
    """Defines the class base model."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
