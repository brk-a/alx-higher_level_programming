#!/usr/bin/python3

'''
Docstring goes here

'''


def inherits_from(obj, a_class):
    ''' inherits_from fn '''
    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
    return False


if __name__ == '__main__':
    inherits_from = __import__('4-inherits_from').inherits_from

    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
