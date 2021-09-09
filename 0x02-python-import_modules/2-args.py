#!/usr/bin/python3


"""
Docstring goes here

"""

if __name__ == '__main__':
    from sys import argv

    num_of_args = len(argv[1:])

    if num_of_args == 0:
        print('0 arguments.')
    elif num_of_args == 1:
        print('1 argument.')
    else:
        print('{:d} arguments.'.format(num_of_args))

    for i, j in enumerate(argv[1:], start=1):
        print('{:d} {:s}'.format(i, j))
