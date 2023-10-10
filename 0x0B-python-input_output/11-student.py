#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs is not None and
                isinstance(attrs, list) and
                all(isinstance(ele, str) for ele in attrs)):
            return {k: getattrs(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
