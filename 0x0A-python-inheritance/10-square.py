#!/usr/bin/python3

'''
Docstring goes here

'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' class Square. Derives from Rect. '''
    def __init__(self, size):
        ''' __init__ method '''
        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        ''' area method '''
        return self.__size ** 2


if __name__ == '__main__':
    Square = __import__('10-square').Square

    s = Square(13)

    print(s)
    print(s.area())
