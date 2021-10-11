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

    def __str__(self):
        ''' __str__ method '''
        return f'[{type(self).__name__}] {self.__size}/{self.__size}'

    def area(self):
        ''' area method '''
        return self.__size ** 2


if __name__ == '__main__':
    Square = __import__('11-square').Square

    s = Square(13)

    print(s)
    print(s.area())
