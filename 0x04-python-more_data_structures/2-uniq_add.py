#!/usr/bin/python3
def uniq_add(my_list=[]):
    """add unique integers only once in a lists."""
    sum = 0
    for i in set(my_list):
        sum += i
    return sum
