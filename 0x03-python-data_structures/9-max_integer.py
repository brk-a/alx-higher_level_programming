#!/usr/bin/python3

"""
Docstring goes hare

"""


def max_integer(my_list=[]):
    int_max = 0
    if len(my_list) == 0:
        return None
    else:
        for i, j in enumerate(my_list):
            if i == 0 or j == int_max:
                int_max = j
        return int_max


if __name__ == '__main__':
    my_list = [i for i in range(100) if i % 2 == 0 and i % 3 == 0]
    max_integer(my_list)
