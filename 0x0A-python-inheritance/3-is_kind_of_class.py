#!/usr/bin/python3

"""Defines class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance or inherited instance of class.

    Arguments:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
