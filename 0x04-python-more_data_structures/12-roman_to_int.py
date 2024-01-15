#!/usr/bin/python3
def roman_to_int(roman_string):
    """ converting a Roman numeral to an integer."""
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    numbers = len(roman_string)
    valuee_int = romans[roman_string[numbers-1]]
    for i in range(numbers - 1, 0, -1):
        new_value = romans[roman_string[i]]
        old_value = romans[roman_string[i-1]]

        if old_value >= new_value:
            valuee_int += old_value
        else:
            valuee_int -= old_value

    return valuee_int
