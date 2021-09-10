#!/usr/bin/python3

"""
Docstring goes here

"""

def new_in_list(my_list, idx, element):
    my_new_list = list(my_list)
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_new_list[idx] = element
        return my_new_list


if __name__ == '__main':
    my_list = [i for i in range(6)]
    idx = 3
    element = 9
    new_in_list(my_list, idx, element)
