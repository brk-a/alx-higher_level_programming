#!/usr/bin/python3

"""
Docstring goes here

"""


def tup_std(tup):
    tup_len = len(tup)
    if tup_len == 0:
        return (0, 0)
    elif tup_len == 1:
        return (tup[0], 0)
    else:
        return (tup[0], tup[1])


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_std = tup_std(tuple_a)
    tuple_b_std = tup_std(tuple_b)
    result = map(lambda i, j: i + j, tuple_a_std, tuple_b_std)
    return tuple(result)


if __name == '__main__':
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    add_tuple(tuple_a, tuple_b)
