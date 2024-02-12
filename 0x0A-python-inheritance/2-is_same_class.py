#!/usr/bin/python3

"""Defines function that checks class."""


def is_same_class(obj, a_class):
    """Check if object is same as instance of given class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to which obj will be matched.
    Returns:
        If obj is same as instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
