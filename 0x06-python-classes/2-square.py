#!/usr/bin/python3
"""Module Square"""


class Square:
    """Represents a square.
    Private instance attribute: size.
    Instantiation with size (with int type/value verification).
    """

    def __init__(self, size=0):
        """intialization of the vars"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
