#!/usr/bin/python3

'''
Docstring goes here

'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' class Rect. Derives from BaseGeom '''
    def __init__(self, width, height):
        ''' __init__  method '''
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' area method '''
        return self.__width * self.__height

    def __str__(self):
        ''' __str__ method '''
        return f'[{type(self).__name__}] {self.__width}/{self.__height}'


if __name__ == '__main__':
    Rectangle = __import__('9-rectangle').Rectangle

    r = Rectangle(3, 5)

    print(r)
    print(r.area())
