#!/usr/bin/python3

"""
Docstring goes here

"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list


if __name__ == '__main__':
    my_list = [i for i in range(6)]
    idx = 3
    element = 9
    print(replace_in_list(my_list, idx, element))
