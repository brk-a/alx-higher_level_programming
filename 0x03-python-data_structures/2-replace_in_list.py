#!/usr/bin/python3

"""
Docstring goes here

"""

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        return my_list[idx] = element


if __name__ == '__main__':
    my_list = [i for i in range(6)]
    idx = 3
    element = 9
    replace_in_list(my_list, idx, element)
