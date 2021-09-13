#!/usr/bin/python3

"""
Docstring goes here

"""


def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for i in range(len(my_list), -1, -1):
            print('{:d}'.format(i))


if __name__ == '__main__':
    my_list = [i for i in range(6)]
    print_reversed_list_integer(my_list)
