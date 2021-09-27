#!/usr/bin/python3

"""
Docstring goes here

"""


def safe_print_division(a, b):
    try:
        result = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        result = None
    finally:
        print('Inside result: {}'.format(result))


if __name__ == '__main__':
    safe_print_division =\
        __import__('3-safe_print_division').safe_print_division

    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
