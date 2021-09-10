#!/usr/bin/python3

"""
Docstring goes here

"""


def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]


if __name__ == '__main__':
    my_list = [i for i in range(6)]
    idx = 3
    print(element_at(my_list, idx))
