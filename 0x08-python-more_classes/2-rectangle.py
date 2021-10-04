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
            raise TypeError(f'height must be >= 0')
        self.__height = height

    def perimeter(self):
        ''' perimeter '''
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def area(self):
        ''' area '''
        return self.__height * self.__width


if __name__ == '__main__':
    Rectangle = __import__('2-rectangle').Rectangle

    my_rect = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rect.area(), my_rect.perimeter()))

    print("--")

    my_rect.width = 10
    my_rect.height = 3
    print("Area: {} - Perimeter: {}".format(my_rect.area(), my_rect.perimeter()))
