#!/usr/bin/python3


"""
Docstring goes here

"""

if __name__ == '__main__':
    from sys import argv

    total = 0
    for i, j in enumerate(argv[1:]):
        total += int(j)
    print(f'{total}')
