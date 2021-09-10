#!/usr/bin/python3

"""
Docstring goes here

"""


def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print('{:d}'.format(i))


if __name__ == '__main__':
    my_list = [i for i in range(6)]
    print_list_integer(my_list)
