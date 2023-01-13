#!/usr/bin/python3

class Base:

    __nb_objects = 0
    def __init__(slef, id=None):
        if id != None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = id
