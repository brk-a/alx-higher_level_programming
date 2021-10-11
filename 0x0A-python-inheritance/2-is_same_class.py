#!/usr/bin/python3

'''
Docstring goes here

'''


def is_same_class(obj, a_class):
    ''' is_same_class fn '''
    if type(obj).__name__ == a_class.__name__:
        return True
    return False


if __name__ == '__main__':
    is_same_class = __import__('2-is_same_class').is_same_class

    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
