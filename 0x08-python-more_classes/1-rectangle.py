#!/usr/bin/python3

'''
Docstring goes here

'''


class Rectangle:
    ''' class Rectangle '''
    def __init__(self, width=0, height=0):
        ''' __init__ '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' width '''
        return self.__width

    @property
    def height(self):
        ''' height '''
        return self.__height

    @width.setter
    def width(self, width):
        ''' width setter '''
        if not isinstance(width, int):
            raise TypeError(f'width must be an integer')
        if width < 0:
            raise ValueError(f'width must be >= 0')
        self.__width = width

    @height.setter
    def height(self, height):
        ''' height setter '''
        if not isinstance(height, int):
            raise TypeError(f'height must be an integer')
        if height < 0:
            raise ValueError(f'height must be >= 0')
        self.__height = height


if __name__ == '__main__':
    Rectangle = __import__('1-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
