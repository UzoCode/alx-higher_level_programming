#!/usr/bin/python3

"""Defines inherited list class MyList."""


class MyList(list):
    """Sorts printing for built-in list class."""

    def print_sorted(self):
        """Print list in sorted ascending order."""
        print(sorted(self))
