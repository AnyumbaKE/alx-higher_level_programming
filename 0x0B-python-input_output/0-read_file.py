#!/usr/bin/python3
"""A function that reads a text file (UTF8)."""


def read_file(filename=""):
    """ Print text file to stdout """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
