#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
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
    #Check if the specified object is an instance of the class
    if isinstance(obj, a_class):
        return True 
    #Check if the specified object is an instance of a
    #class that inherited from the specified class
    else:
        return isinstance(obj.__class__.__bases__, a_class)
