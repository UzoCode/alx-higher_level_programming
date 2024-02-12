#!/usr/bin/python3

"""To defines inherited class-checking function."""

def inherits_from(obj, a_class):
    """Checks if object is an inherited instance of a class.

    Argument:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
