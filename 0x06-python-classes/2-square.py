#!/usr/bin/python3
""" This class Square defines a square"""


class Square():
    """square class with size and proper validation"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size