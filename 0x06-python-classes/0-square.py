#!/usr/bin/python3


"""
Class Square

Creates an instance of a square

"""


class Square:
    pass


if __name__ == '__main__':
    Square = __import__('0-square').Square

    my_square = Square()
    print(type(my_square))
    print(my_square.__dict__)
