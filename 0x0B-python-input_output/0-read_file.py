#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    """reads file with a file discripter"""
    with open(filename, 'r', encoding='utf8') as file:
        r_file = file.read()
        print(r_file, end='')
