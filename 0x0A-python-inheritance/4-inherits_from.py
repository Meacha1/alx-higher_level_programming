#!/usr/bin/python3
"""
Returns True if the object is an instance of a class that inherited (directly or indirectly)
from the specified class; otherwise False.

Parameters:
obj (object): The object to check.
a_class (class): The class to check against.

Returns:
bool: True if the object is an instance of a class that inherited from the specified class;
      False otherwise.
"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
