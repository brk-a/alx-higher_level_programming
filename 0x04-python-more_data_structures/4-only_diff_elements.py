#!/usr/bin/python3

"""
Docstring goes here

"""


def common_elements(set_1, set_2):
    set_1 = set_1 if set_1 and type(set_1) == set else set()
    set_2 = set_2 if set_2 and type(set_2) == set else set()
    return set_1 ^ set_2

if __name__ =='__main__':
    set_1 = {'cheesy', 'chilli', 'chunky', 'chutney'}
    set_2 = {'coleslaw', 'couscous', 'cheesy', 'chunky'}
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
