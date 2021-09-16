#!/usr/bin/python3

"""
Docstring goes here

"""


def roman_to_int(roman_string):
    roman_string = roman_string.upper() if roman_string \
                   and type(roman_string) == str else ''
    if roman_string == None or roman_string == '':
        return 0
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    roman_string = roman_string.replace("IV", "IIII").replace("IX", "VIIII")
    roman_string = roman_string.replace("XL", "XXXX").replace("XC", "LXXXX")
    roman_string = roman_string.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in roman_string:
        number += translations[char]
    return number


if __name__ == '__main__':
    """ Roman to Integer test file
    """
    roman_to_int = __import__('12-roman_to_int').roman_to_int

    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "CM"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "XCIX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
