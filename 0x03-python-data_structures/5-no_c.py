#!/usr/bin/python3

"""
Docstring goes here

"""


def no_c(my_string):
    new_str = ''
    for i in my_string:
        if i not in ('c', 'C'):
            new_str += i
    return new_str


if __name__ == '__main__':
    my_string = 'Cheeky cheetah, chunky chinchilla, cheesy cheesy chizi'
    no_c(my_string)
