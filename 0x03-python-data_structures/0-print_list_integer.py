#!/usr/bin/python3

"""
Docstring goes here

"""


def print_list_integer(my_list=[]):
    my_list = my_list if my_list and type(my_list) is list else []
    for i in my_list:
        print('{:d}'.format(i))


if __name__ == '__main__':
    my_list = [i for i in range(6)]
    print_list_integer(my_list)
