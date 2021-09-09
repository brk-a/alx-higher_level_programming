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
        print(f'1: {agrv[1]}')
    else:
        print(f'{num_of_args} arguments.')
        for i in range(2: num_of_args):
            print(argv[i])
