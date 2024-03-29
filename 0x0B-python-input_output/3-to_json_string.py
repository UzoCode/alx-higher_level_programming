#!/usr/bin/python3

"""A string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of string object."""
    return json.dumps(my_obj)
