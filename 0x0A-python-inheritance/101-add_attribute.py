#!/usr/bin/python3
"""A function that adds a new attribute to an object if it’s possible:"""


def add_attribute(obj, attribute, value):
    """add a new attribute to object if possible"""
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
