#!/usr/bin/python3

"""
Docstring goes here

"""


def multiply_list_map(my_list=[], number=0):
    my_list = my_list if my_list and type(my_list) == list else []
    return list(map(lambda x: x * number, list(my_list)))

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 6]
    new_list = multiply_list_map(my_list, 4)
    print(new_list)
    print(my_list)
