#!/usr/bin/python3

"""To define Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initializes new square.

        Arguments:
            size (int): Size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
