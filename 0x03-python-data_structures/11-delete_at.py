#!/usr/bin/python3

"""
Docstring goes here

"""


def delete_at(my_list=[], idx=0):
    my_list = my_list if my_list and type(my_list) is list else []
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list = [my_list[i] for i in range(len(my_list)) if i != idx]
        return my_list


if __name__ == '__main__':
    my_list = [i for i in range(101)]
    idx = 3
    print(delete_at(my_list, idx))
