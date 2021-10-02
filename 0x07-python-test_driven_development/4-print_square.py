#!/usr/bin/python3

'''
Docstring goes here

'''


def print_square(size):
    '''print sq'''
    if size < 0:
        raise ValueError('size must be >= 0')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if not isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if size == 0:
        print()
    if size > 0:
        for i in range(size):
            print('#' * size)


if __name__ == '__main__':
    print_square = __import__('4-print_square').print_square

    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
