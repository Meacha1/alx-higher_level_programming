#!/usr/bin/python3

class MyList(list):
"""
class called MyList
"""
    def print_sorted(self):
    """prints a sorted List"""
        self.sort()
        print(self)
