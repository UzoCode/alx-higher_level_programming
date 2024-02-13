#!/usr/bin/python3

"""Text file-reading function."""

def read_file(filename=""):
    """Prints content of UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
