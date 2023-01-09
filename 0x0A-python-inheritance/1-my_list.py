#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """subclass called MyList"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted List"""
        self.sort()
        print(self)
