#!/usr/bin/python3
"""
This function returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class; otherwise False
    
Arguments:
    obj : The specified object
    a_class: The class to compare against
    
Returns:
    True or False
"""
def is_kind_of_class(obj, a_class):
    """True if obj is an instance or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
