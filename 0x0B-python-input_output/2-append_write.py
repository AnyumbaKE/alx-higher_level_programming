#!/usr/bin/python3
"""
Defines a function that appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """Returns the number of characters added:"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
