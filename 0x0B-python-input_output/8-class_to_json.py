#!/usr/bin/python3

"""A Python class-to-JSON function."""

def class_to_json(obj):
    """Returns dictionary representation of simple data structure."""
    return obj.__dict__
