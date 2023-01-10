#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    """reads file with a file discripter"""
    with open(filename, 'r', encoding='utf8') as file:
    """reads a file a print out to stdout"""
        for line in file:
            print(line)
