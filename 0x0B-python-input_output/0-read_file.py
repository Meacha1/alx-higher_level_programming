#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r', encoding='utf8') as file:
        for line in file:
            print(line)
