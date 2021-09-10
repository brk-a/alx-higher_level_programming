#!/usr/bin/python3

"""
Docstring goes here

"""


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_li = [my_list[i] for i in range(len(my_list)) if i != idx]
        return new_li


if __name__ == '__main__':
    my_list = [i for i in range(101)]
    idx = 3
    print(f'{delete_at(my_list, idx)}')
