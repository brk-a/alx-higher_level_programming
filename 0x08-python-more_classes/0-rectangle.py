#!/usr/bin/python3

'''
Docstring goes here

'''


class Rectangle:
    '''class rectangle'''
    pass


if __name__ == '__main__':
    Rectangle = __import__('0-rectangle').Rectangle

    my_rectangle = Rectangle()
    print(type(my_rectangle))
    print(my_rectangle.__dict__)
