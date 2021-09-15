#!/usr/bin/python3

"""
Docstring goes here

"""


def uniq_add(my_list=[]):
    my_list = my_list if my_list and type(my_list) == list else []
    total = sum(set(my_list))
    return total


if __name__ == '__main__':
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
